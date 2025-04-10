import dash
from dash import html, Dash, dcc

app = Dash(__name__, use_pages = True, suppress_callback_exceptions = True)

app.layout = html.Div([
    html.H1('Dashboard'),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']}", href=f"{page['relative_path']}"),
        ) for page in dash.page_registry.values()
    ]),
    dash.page_container
])

if __name__ == '__main__':
    app.run(debug = True)
