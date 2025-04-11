from dash import html, dcc
import dash_bootstrap_components as dbc

from utils.data_preparer import DataPreparer

data_preparer = DataPreparer()

unique_fy = data_preparer.get_col_unique_values("merged", "payment_date_fy", sort_desc = True)

# One for the World color palette
colors = {
    'primary': '#006466',     # Teal/blue-green
    'secondary': '#065A60',   # Darker teal
    'accent': '#0B525B',      # Another shade
    'light': '#144552',       # Lighter shade
    'text': '#1B3A4B',        # For text
    'highlight': '#F2F2F2',   # Light highlight
    'white': '#FFFFFF'
}

def page1_layout():
    return html.Div(
        children = [
            html.H1("One for the World", style={'textAlign': 'center', 'color': colors['text'], 'marginBottom': '10px'}),
            # -- Filters --
            html.Div(
                children = [
                    html.Div(
                        children = [
                            html.Span(
                                "Select FY",
                                className="d-block fw-medium mb-1",
                            ),
                            dcc.Dropdown(
                                id="fy-filter",
                                options=[
                                    dict(
                                        label=fy,
                                        value=fy,
                                    )
                                    for fy in unique_fy
                                ],
                                placeholder="Select FY",
                                multi=False,
                                value=unique_fy[0],
                                clearable=False,
                            ),
                        ]
                    )
                ]
            ),
            # -- End of Filters --

            # -- KPI Cards --
            html.Div(
                children = [
                    html.Div(
                        id = "money-moved-card",
                        style = {
                            'backgroundColor': colors['highlight'], 
                            'borderRadius': '10px', 
                            'marginBottom': '20px', 
                            'padding': '15px',
                            'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)'
                        }
                    ),
                    html.Div(
                        id = "cf-money-moved-card",
                        style = {
                            'backgroundColor': colors['highlight'], 
                            'borderRadius': '10px', 
                            'marginBottom': '20px', 
                            'padding': '15px',
                            'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)'
                        }
                    ),
                    html.Div(
                        # id = "cf-money-moved-card",
                        style = {
                            'backgroundColor': colors['highlight'], 
                            'borderRadius': '10px', 
                            'marginBottom': '20px', 
                            'padding': '15px',
                            'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)'
                        }
                    ),
                ],
                style={
                    'display': 'flex',
                    # 'justifyContent': 'center',
                    'gap': '20px',  # adds space between cards
                    'flexWrap': 'wrap'  # allows wrapping on smaller screens
                },
            ),

            # -- End of KPI Cards --
        
            # -- Graphs --
            html.Div(
                className = "row gy-4",
                children = [
                    html.Div(
                        className="col-xxl-7 col-md-7 col-xs-12 col-sm-12 col-xl-12 ",
                        children=[
                            html.Div(
                                className="card h-100",
                                children=[
                                    html.Div(
                                        className="card-body",
                                        children=[
                                            html.Div(
                                                className="card-title d-flex align-items-center mb-4",
                                                children=[
                                                    html.Div(
                                                        className="avatar me-2",
                                                        children=[
                                                            html.Span(
                                                                className="avatar-initial rounded-2 bg-label-success",
                                                                children=[
                                                                    html.I(
                                                                        className="bx bx-trending-up bx-lg text-success"
                                                                    )
                                                                ],
                                                            )
                                                        ],
                                                    ),
                                                    html.Div(
                                                        children=[
                                                            html.H6(
                                                                "Money Moved Monthly",
                                                                className="text-lg mb-3 ml-1",
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            html.Div(
                                                className="table bordered-table mb-0 dataTable",
                                                children=[
                                                    dcc.Graph(
                                                        id = "money-moved-graph",
                                                        style = {
                                                            'backgroundColor': colors['white'], 
                                                            'borderRadius': '10px', 
                                                            'padding': '15px',
                                                            'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)'
                                                        }
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                    html.Div(
                        className="col-xxl-7 col-md-7 col-xs-12 col-sm-12 col-xl-12 ",
                        children=[
                            html.Div(
                                className="card h-100",
                                children=[
                                    html.Div(
                                        className="card-body",
                                        children=[
                                            html.Div(
                                                className="card-title d-flex align-items-center mb-4",
                                                children=[
                                                    html.Div(
                                                        className="avatar me-2",
                                                        children=[
                                                            html.Span(
                                                                className="avatar-initial rounded-2 bg-label-success",
                                                                children=[
                                                                    html.I(
                                                                        className="bx bx-trending-up bx-lg text-success"
                                                                    )
                                                                ],
                                                            )
                                                        ],
                                                    ),
                                                    html.Div(
                                                        children=[
                                                            html.H6(
                                                                "Counterfactual Money Moved Monthly",
                                                                className="text-lg mb-3 ml-1",
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            html.Div(
                                                className="table bordered-table mb-0 dataTable",
                                                children=[
                                                    dcc.Graph(
                                                        id = "cf-money-moved-graph",
                                                        style = {
                                                            'backgroundColor': colors['white'], 
                                                            'borderRadius': '10px', 
                                                            'padding': '15px',
                                                            'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)'
                                                        }
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                ]
            ),
            html.Div(
                className = "row gy-4",
                children = [
                    html.Div(
                        className="col-xxl-7 col-md-7 col-xs-12 col-sm-12 col-xl-12 ",
                        children=[
                            html.Div(
                                className="card h-100",
                                children=[
                                    html.Div(
                                        className="card-body",
                                        children=[
                                            html.Div(
                                                className="card-title d-flex align-items-center mb-4",
                                                children=[
                                                    html.Div(
                                                        className="avatar me-2",
                                                        children=[
                                                            html.Span(
                                                                className="avatar-initial rounded-2 bg-label-success",
                                                                children=[
                                                                    html.I(
                                                                        className="bx bx-trending-up bx-lg text-success"
                                                                    )
                                                                ],
                                                            )
                                                        ],
                                                    ),
                                                    html.Div(
                                                        children=[
                                                            html.H6(
                                                                "Counterfactual Money Moved Monthly",
                                                                className="text-lg mb-3 ml-1",
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            html.Div(
                                                className="table bordered-table mb-0 dataTable",
                                                children=[
                                                    dcc.Graph(
                                                        id = "money-moved-mosaic-graph",
                                                        style = {
                                                            'backgroundColor': colors['white'], 
                                                            'borderRadius': '10px', 
                                                            'padding': '15px',
                                                            'boxShadow': '0 4px 6px rgba(0, 0, 0, 0.1)'
                                                        }
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            )
        ]
    )