# import Libraries
import dash
import base64
import io
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from dash import Dash, html, dcc, callback, Output, Input, State
from graph import displayPostags, calculatedataframe, missingHeatmap
from process_files import get_text_chunks, get_vectorstore, handleQuestion, processCSV, decode_csv, countWords




# // initialize the app
app = Dash(__name__)

# // dfine the app layput
app.layout = html.Div([
    # //  header with logo and tittle
    html.Div([
        html.Img(src="/assets/logo.png", id='logo'),
        html.H1("Welcome to FilesInsights!", id="title")
    ], className='header'),

    # //Tabs and file uploader side by side
    html.Div([
        html.Div([
            html.Div(id='uploaded-files'),
            # // document uploader
            dcc.Upload(
                id='file-upload',
                children=html.Button('Browse', className="Br_button"),
                multiple=True
            ),
            
        ], className='file-uploader'),

        html.Div([
            # //Tabs
            dcc.Tabs(id='tabs', value='tab-1', children=[
                dcc.Tab(label='Question and Answer', value='tab-1', children =[
                    html.Div([
                        html.Label('Type your question and press Enter:'),
                        dcc.Input(id='question-input', type='text', placeholder='Type your question...')], className='text_Input'),
                ], className='tab-header'),
                dcc.Tab(label='Charts and Graphs', value='tab-2', className='tab-header')
            ]),
            # // Tabs content
            html.Div(id='tab-content')
        ], className='tabs')
    ], className='side-by-side')  # Apply CSS class 'side-by-side' to arrange elements side by side
 

])                  # // ends layout

# // callbacks
    
# // callback to update filenames
@app.callback(Output('uploaded-files', 'children'),
              Input('file-upload', 'filename'))
def display_uploaded_filenames(filenames):
    if filenames is not None:
        return [html.H5(f'{f}') for f in filenames]
    else:
        return 'No File Uploaded. Please upload only similar types of files such as all Pdfs or all csvs for multiple files. It only supports Pdf and csv'
    


# // callback to process files
@app.callback(Output('tab-content', 'children'),
              Input('question-input', 'n_submit'),
              Input('tabs', 'value'),
              State('question-input','value'),
              State('file-upload', 'contents'),
              State('file-upload', 'filename'),
              )
def process_uploaded_files(n_submit, tab_value, question, contents, filenames):
    if contents is not None and len(contents) > 0:
        text = ""  # Create an empty text string to store the combined text from all PDFs
        csv_data = []  # Create a dictionary to store data from CSV files

        for content_data, filename in zip(contents, filenames):
            # Check if the file is a PDF
            if 'pdf' in filename.lower():
                content_type, content_string = content_data.split(',')
    
                decoded = base64.b64decode(content_string)
                
                pdf = PdfReader(io.BytesIO(decoded))

                # Extract text from each page of the PDF
                for page in range(len(pdf.pages)):
                    text += pdf.pages[page].extract_text()
                # print(text)
            
            elif 'csv' in filename.lower():
                content_type, content_string = content_data.split(',')
                decoded_csv = base64.b64decode(content_string)
                df1 = decode_csv(decoded_csv)
                csv_data.append(df1)

            else:
                print('Not a PDF or csv file')
            
           

  

    else:
        print('No content uploaded.')

    # update tabs
    if tab_value == 'tab-1':
        if n_submit is not None and n_submit > 0 and question:
            for filename in filenames:
                # Check if the file is a PDF
                if 'pdf' in filename.lower():
                    # create chunks of the text data
                    text_chunks = get_text_chunks(text)

                    # create vectorstore
                    vectorstore = get_vectorstore(text_chunks)
        
                    answer = handleQuestion(question, vectorstore)
                    # print(answer['question'])
                    # print(answer['answer'])

                elif 'csv' in filename.lower():
                    # Iterate over the DataFrames in the dictionary
                    # for key, df in csv_data.items():
                    answer = processCSV(csv_data, question)
        
                else:
                    print('Not a proper type')
    
                return html.Div([html.Div([
                    html.Div(html.Img(src='/assets/user.png', alt='User', className='image')),
                    html.Div(answer['question'], className="question-output")], className='user-container'),

                    html.Div([html.Div(html.Img(src='/assets/logo.png', alt='Bot', className='image')),
                            html.Div(answer['answer'], className="answer-output")], className='bot-container')
                            ], className="output-container")
            
    elif tab_value == 'tab-2':
        # print('Hi its tab 2')
        if n_submit is not None and n_submit > 0 and question:
            # print('yes')
            if any('pdf' in filename.lower() for filename in filenames):
                num_chars, num_words, num_sents, pos_tags_count = countWords(text)
                # print(pos_tags_count)
                posfig = displayPostags(pos_tags_count)
                return html.Div([
                    html.Div(children=[
                        html.Div(children=[html.H3(num_chars), html.H3('Number of Characters')], className='topper'),
                        html.Div(children=[html.H3(num_words), html.H3('Number of Words')], className='topper'),
                        html.Div(children=[html.H3(num_sents), html.H3('Number of Sentences')], className='topper'),
                    ], className='topper-output'),
                    html.Div(children=[
                        html.Div(children=[html.Div(dcc.Graph(figure=posfig))], className='mid-graph1'),
                        # html.Div(children=[], className='mid-graph2'),
                    ], className='middle-output'),
                    
                ], className='graph-container')
            
            # for csv files
            if any('csv' in filename.lower() for filename in filenames):
                rows, cols, missing = calculatedataframe(csv_data)
                # heatmap
                heatmap = missingHeatmap(csv_data)

                return html.Div([
                    html.Div(children=[
                        html.Div(children=[html.H3(rows), html.H3('Number of Rows')], className='topper'),
                        html.Div(children=[html.H3(cols), html.H3('Number of Columns')], className='topper'),
                        html.Div(children=[html.H3(missing), html.H3('Missing Values')], className='topper'),
                    ], className='topper-output'),
                    html.Div(children=[
                        html.Div(children=[html.Div(dcc.Graph(figure=heatmap))], className='mid-graph1'),
                    ], className='middle-output'),
                    
                ], className='graph-container')

    else:
        pass
            


        
# // run the app
if __name__ == '__main__':
    app.run(debug=True)