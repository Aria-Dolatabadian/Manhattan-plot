# Your own data can be uploaded on Github (in a repository) first and then raw data link be used. 
#  https://dash.plotly.com/dash-bio/manhattanplot

import pandas as pd
import dash
from dash.dependencies import Input, Output
import dash_bio as dashbio
from dash import html, dcc

app = dash.Dash(__name__)

df = pd.read_csv('https://git.io/manhattan_data.csv')

app.layout = html.Div([
    'Threshold value',
    dcc.Slider(
        id='default-manhattanplot-input',
        min=1,
        max=10,
        marks={
            i: {'label': str(i)} for i in range(10)
        },
        value=4
    ),
    html.Br(),
    html.Div(
        dcc.Graph(
            id='default-dashbio-manhattanplot',
            figure=dashbio.ManhattanPlot(
                dataframe=df
            )
        )
    )
])

@app.callback(
    Output('default-dashbio-manhattanplot', 'figure'),
    Input('default-manhattanplot-input', 'value')
)
def update_manhattanplot(threshold):

    return dashbio.ManhattanPlot(
        dataframe=df,
        genomewideline_value=threshold
    )

if __name__ == '__main__':
    app.run_server(debug=True)
