import dash
from dash import html

# dash.register_page(__name__, path = '/page2')

def layout(**kwargs):
    return html.Div([
        html.H1('This is page2'),
    ])
