from flask import Flask, render_template
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

server = Flask(__name__)
app = Dash(__name__, server=server, url_base_pathname='/dashboard/')

# Sample data
data = {'x': [1, 2, 3, 4, 5], 'y': [10, 11, 12, 13, 14]}

app.layout = html.Div([
    html.H1("Flask Dashboard with Dash"),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': data['x'], 'y': data['y'], 'type': 'line', 'name': 'Line Chart'},
            ],
            'layout': {
                'title': 'Sample Line Chart',
            }
        }
    ),

    dcc.Slider(
        id='slider',
        min=1,
        max=10,
        step=1,
        value=5,
        marks={i: str(i) for i in range(1, 11)},
    ),

    html.Div(id='slider-output')
])

@app.callback(
    Output('slider-output', 'children'),
    [Input('slider', 'value')]
)
def update_output(value):
    return f'Slider Value: {value}'


@server.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    server.run()