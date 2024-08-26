import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

def fetch_financial_data(company='AMZN'):
    """
    This function fetch stock market quotations.
    """
    import pandas_datareader.data as web
    return web.DataReader(name=company, data_source='stooq')

df = fetch_financial_data()
df.reset_index(inplace=True)
df = df[df['Date'] >= datetime.now() - timedelta(days=365)]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.H4('Amazon stock quote'),

    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Scatter(
                    x=np.array(df.Date),
                    y=df.Close,
                    mode='lines',
                    fill='tozeroy',
                    name='Amazon'
                )
            ],
            layout=go.Layout(
                yaxis_type='log',
                height=500,
                title_text='Stock price plot',
                showlegend=True
            )
        )
    ),

    dcc.Graph(
        figure=go.Figure(
            data=[
                go.Bar(
                    x=np.array(df.Date),
                    y=df.Volume,
                    name='Volume'
                )
            ],
            layout=go.Layout(
                yaxis_type='log',
                height=300,
                title_text='Volume plot',
                showlegend=True
            )
        )
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
