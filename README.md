# FilesInsights

# Introduction
<p>FilesInsights is a web application developed using Plotly Dash, Langchain, and OpenAI that offers a wide range of features for processing and exploring PDF and CSV files. This README provides an overview of the application and its functionality.</p>

# Features
<p>FilesInsights comes with the following features:</p>
1. <b>File Upload:</b> Users can upload PDF and CSV files, and the system automatically detects the file type for further processing.<br>
2. <b>Question and Answer: </b> The 'Question and Answer' tab allows users to input questions about the uploaded files. After submitting a question, the system processes it and provides an answer.<br>
3. <b>Charts and Graphs:</b> Users can navigate to the 'Charts and Graphs' tab, which offers various pre-built charts for visualizing the data in the uploaded files.<br>
4. <b>File Compatibility:</b> FilesInsights currently supports PDF and CSV file types. The application is designed to expand its capabilities to accommodate additional file formats in the future.<br>
5. <b>Enhancements:</b> The development team is actively working on enhancing the charting and graphing options to provide users with more data visualization tools.<br>
6. <b>Plotly Dash Framework:</b> FilesInsights is built using the Plotly Dash framework, ensuring a smooth and interactive user experience.<br>



# Getting Started
 <p>To run FilesInsights on your local machine, follow these steps:</p>
1. Clone the repository to your local machine.
   ```
    git clone https://github.com/AliNaqvi110/Multiple-Files-QA-and-Insights-Using-OpenAI.git
   ```


2. Install the required dependencies by running the following command:

    ```
    pip install -r requirements.txt
    ```

3. Obtain an API key from OpenAI and add it to the `.env` file in the project directory.

    ```shell
    OPENAI_API_KEY=your_secret_api_key
    ```
4. Run the App
 Execute the app using the command.
 
    ```
    python app.py runserver 8050
    ```
 This will launch the App interface in your web browser.
5. <b> Access the Application:</b> Open a web browser and navigate to the specified address (e.g., http://localhost:8050) to access FilesInsights.

## Usage
<p>Upon accessing the application, users can easily upload files and explore their content. Here are some tips to get started:</p>
1. Use the 'File Upload' section to upload PDF and CSV files.

2. In the 'Question and Answer' tab, enter your questions and press 'Enter' to receive answers based on the file content.

3. Visit the 'Charts and Graphs' tab to view pre-built charts and graphs generated from the uploaded files.

## Contributing
<p>We welcome contributions from the community to improve and expand FilesInsights. If you have suggestions or would like to contribute, please create a pull request or open an issue.</p>

## License
<p>FilesInsights is licensed under the MIT License.</p>

## Acknowledgments
<p>We would like to express our gratitude to the open-source community for the tools and libraries that make this project possible. Special thanks to the creators of Plotly Dash and Langchain for their outstanding work.</p>
