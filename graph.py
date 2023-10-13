# // import libraries
import plotly.graph_objects as go
# // function for display top KPIS
def displayPostags(pos_tags_count):
    # Separate the keys and values from the dictionary
    keys = list(pos_tags_count.keys())
    values = list(pos_tags_count.values())
    # Create a bar graph
    fig = go.Figure(data=[go.Bar(x=keys, y=values, text=values, textposition='inside')])
    # Set the layout
    fig.update_layout(
        title='Frequency of Parts of Speech',
        xaxis_title='Pos Tag Name',
        yaxis_title='Pos Tag count',
        )
    return fig

# // function to calculate num of rows,cols and missing values in dataframes
def calculatedataframe(dataframes):
    total_rows = 0
    total_cols = 0
    total_missing = 0
    for dataframe in dataframes:
        total_rows += len(dataframe)
        total_cols += len(dataframe.columns)
        total_missing += dataframe.isnull().sum().sum()
    return total_rows, total_cols, total_missing

# // missing values heatmap
def missingHeatmap(data):
    df1 = data[0]
    missing = df1.isna().sum()
    fig = go.Figure(data=[
        go.Heatmap(z=missing)
        ])
    fig.update_layout(
        title='Missing Values Heatmap',
        )
    return fig