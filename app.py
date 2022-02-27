import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepe.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.DataFrame({"fruit":['apples','oranges','bananas','apples','oranges','bananas'],
                    'amount':[4,5,2,2,4,1],
                    'city':['SF','SF','SF','Montreal','Montreal','Montreal']})

fig = px.bar(df, x='fruit',y='amount',color='city',barmode = 'group')

app.layout = html.Div(children=[
            html.H1(children='hello dash'),

            html.Div(children='''
            Dash: A web application framework for Python.
            '''),
            dcc.Graph(
                    id='example-graph',
                    figure=fig
            )
        ])

if __name__ == '__main__':
    app.run_server(debug=True)

server = app.server