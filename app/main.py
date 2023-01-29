import psycopg2
import dash
from dash import dcc, html
import pandas as pd

# Connect to the PostgresSQL database and retrieve data
conn = psycopg2.connect(
    host="168.119.35.175",
    port=5433,
    user="candidato",
    password="crossnection21",
    database="auto"
)
query = "SELECT * FROM auto"
df = pd.read_sql(query, conn)

# Get the list of numerical columns
num_cols = df.select_dtypes(include='number').columns.tolist()

# Create the Dash app
app = dash.Dash()
app.layout = html.Div([
    html.Div([
    html.Label('Select X variable:'),
    dcc.Dropdown(
        id='x-col',
        options=[{'label': col, 'value': col} for col in num_cols],
        value=num_cols[0]
    ),
    html.Label('Select Y variable:'),
    dcc.Dropdown(
        id='y-col',
        options=[{'label': col, 'value': col} for col in num_cols],
        value=num_cols[1]
    )],
    style={
        "width": "25%",
        "margin": "14em 1em",
        "display": "inline-block"}
    ),
    html.Div([
        dcc.Graph(id='scatter-plot')
    ],
    style={
        "width": "70%",
        "margin-top": "5em",
        "float": "right",
        "display": "inline-block"}
    )
])

# Update the scatter plot based on the selected columns
@app.callback(
    dash.dependencies.Output('scatter-plot', 'figure'),
    [dash.dependencies.Input('x-col', 'value'),
     dash.dependencies.Input('y-col', 'value')]
)
def update_scatter_plot(x_col, y_col):
    return {
        'data': [{
            'x': df[x_col],
            'y': df[y_col],
            'type': 'scatter'
        }],
        'layout': {
            'title': f'{x_col} vs {y_col}'
        }
    }

# Run app   
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8050)

# Close connection to db
conn.close()