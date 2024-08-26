import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go

app = dash.Dash(__name__) # app instance

# html section
app.layout = html.Div(children=[
    html.H2(children='Hello Dash, Hello world!'),
    html.P(children='Ladies and gentleman, this bar plot presents the sales value in a certain fictional trade company:'),
    dcc.Graph(figure=go.Figure([
        go.Bar(
        x=[2022, 2023, 2024],
        y=[785, 1208, 2018],
        name='Local'),
        go.Bar(
            x=[2022, 2023, 2024],
            y=[1230, 1480, 1892],
            name='Online'
        )]
        )
    ),
    html.H2(children='Thank you for your attention!')
])

if __name__ == '__main__':
    app.run_server(debug=True)
