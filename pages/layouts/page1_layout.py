from dash import html, dcc
import dash_bootstrap_components as dbc

import dash_draggable

from utils.data_preparer import DataPreparer

data_preparer = DataPreparer()

unique_fy = data_preparer.get_col_unique_values(
    "merged", "payment_date_fy", sort_desc=True
)

unique_platforms = data_preparer.get_col_unique_values("merged", "payment_platform")
unique_chapter_types = data_preparer.get_col_unique_values(
    "merged", "pledge_chapter_type"
)

drilldown_by = [
    {"label": "Payment Platform", "value": "payment_platform"},
    {"label": "Source (Chapter Types)", "value": "pledge_chapter_type"},
]

# One for the World color palette
colors = {
    "primary": "#006466",  # Teal/blue-green
    "secondary": "#065A60",  # Darker teal
    "accent": "#0B525B",  # Another shade
    "light": "#144552",  # Lighter shade
    "text": "#1B3A4B",  # For text
    "highlight": "#F2F2F2",  # Light highlight
    "white": "#FFFFFF",
}


def chart_header_title_with_ai(chart_id, title):
    component = html.Div(
        className="d-flex justify-content-between align-items-center w-100",
        children=[
            dbc.Row(
                class_name="d-flex justify-content-between align-items-center w-100",
                children=[
                    dbc.Col(html.H6(title, className="mb-0"), width="auto"),
                    dbc.Col(
                        html.Div(
                            html.I(
                                children=[
                                    html.Span(
                                        className="ripple",
                                    ),  # Add your desired content inside the span
                                ],
                                className="bi bi-magic position-relative",
                                id={"type": "ai-icon", "chart": chart_id},
                                style={
                                    "cursor": "pointer",
                                    "fontSize": "1.3rem",
                                    "color": "#065A60",
                                },
                            ),
                            style={"textAlign": "right"},
                        ),
                        width="auto",
                    ),
                ],
                justify="between",
                align="center",
                className="mb-2",
            ),
            dbc.Tooltip(
                "Click here for Actionable Insights (AI)",
                target={"type": "ai-icon", "chart": chart_id},
                placement="top",
            ),
        ],
    )

    return component


def page1_layout():
    return html.Div(
        children=[
            html.Div(
                className="layout-navbar-fixed layout-menu-fixed layout-wide",
                dir="ltr",
                children=[
                    html.Div(
                        className="layout-wrapper layout-navbar-full layout-horizontal layout-without-menu",
                        children=[
                            html.Div(
                                className="layout-container",
                                children=[
                                    html.Div(
                                        className="layout-page",
                                        children=[
                                            # Content Wrapper
                                            html.Div(
                                                className="content-wrapper",
                                                children=[
                                                    html.Header(
                                                        id="main-header",
                                                        children=[
                                                            html.Div(
                                                                html.Img(
                                                                    src="../../assets/img/illustrations/one_of_the_world_logo.png",
                                                                    height="55",
                                                                    className="scaleX-n1-rtl logotext",
                                                                    alt="View Badge User",
                                                                ),
                                                                className="logo",
                                                            ),
                                                        ],
                                                    ),
                                                    html.Div(
                                                        className="container-fluid flex-grow-1 container-p-y p-top-custom",
                                                        children=[
                                                              html.Div(
                                                                className="row gy-4 mt-1 mb-4",
                                                                children=[
                                                                    html.Div(
                                                                        className="col-lg-4 col-md-4  align-self-end order-4",
                                                                        children=[
                                                                            html.Div(
                                                                                className="card back-color",
                                                                                children=[
                                                                                    html.Div(
                                                                                        className="d-flex row",
                                                                                        children=[
                                                                                            html.Div(
                                                                                                className="col-sm-3 col-md-3 text-center text-sm-left d-flex align-items-center",
                                                                                                children=[
                                                                                                    html.Div(
                                                                                                        className="card-body pb-0 text-sm-start text-center",
                                                                                                        children=[
                                                                                                            html.Img(
                                                                                                                src="../../assets/img/illustrations/OFTW-Logomark-Logo.png",
                                                                                                                height="120",
                                                                                                                alt="Target User",
                                                                                                            )
                                                                                                        ],
                                                                                                    )
                                                                                                ],
                                                                                            ),
                                                                                            html.Div(
                                                                                                className="col-sm-9 col-md-9 pl-0",
                                                                                                children=[
                                                                                                    html.Div(
                                                                                                        className="card-body right-bg h-100",
                                                                                                        id="money-moved-card",
                                                                                                        children=[
                                                                                                            html.H5(
                                                                                                                "Welcome!",
                                                                                                                className="card-title txt-primary mb-2",
                                                                                                            ),
                                                                                                            html.H4(
                                                                                                                "One for the World",
                                                                                                                className="mb-6 txt-orange",
                                                                                                            ),
                                                                                                            # html.Span(
                                                                                                            #     "78% of TARGET",
                                                                                                            #     className="badge bg-label-primary",
                                                                                                            # ),
                                                                                                        ],
                                                                                                    )
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                    )
                                                                                ],
                                                                            )
                                                                        ],
                                                                    ),
                                                                    html.Div(
                                                                        className="col-lg-4 col-md-4  align-self-end order-4",
                                                                        children=[
                                                                            html.Div(
                                                                                className="card back-color-yellow",
                                                                                children=[
                                                                                    html.Div(
                                                                                        className="d-flex row",
                                                                                        children=[
                                                                                            html.Div(
                                                                                                className="col-sm-3 col-md-3 text-center text-sm-left",
                                                                                                children=[
                                                                                                    html.Div(
                                                                                                        className="card-body pb-0  d-flex align-items-center text-sm-start text-center",
                                                                                                        children=[
                                                                                                            html.Img(
                                                                                                                src="../../assets/img/illustrations/OFTW-Logomark-Logo.png",
                                                                                                                height="120",
                                                                                                                alt="Target User",
                                                                                                            )
                                                                                                        ],
                                                                                                    )
                                                                                                ],
                                                                                            ),
                                                                                            html.Div(
                                                                                                className="col-sm-9 col-md-9",
                                                                                                children=[
                                                                                                    html.Div(
                                                                                                        className="card-body right-bg-yellow h-100",
                                                                                                        id="cf-money-moved-card",
                                                                                                        children=[
                                                                                                        ],
                                                                                                    )
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                    )
                                                                                ],
                                                                            )
                                                                        ],
                                                                    ),
                                                                    html.Div(
                                                                        className="col-lg-4 col-md-4 align-self-end order-4",
                                                                        children=[
                                                                            html.Div(
                                                                                className="card back-color-blue",
                                                                                children=[
                                                                                    html.Div(
                                                                                        className="d-flex row",
                                                                                        children=[
                                                                                            html.Div(
                                                                                                className="col-sm-3 col-md-3 text-center text-sm-left",
                                                                                                children=[
                                                                                                    html.Div(
                                                                                                        className="card-body pb-0 d-flex align-items-center text-sm-start text-center",
                                                                                                        children=[
                                                                                                            html.Img(
                                                                                                                src="../../assets/img/illustrations/OFTW-Logomark-Logo.png",
                                                                                                                height="120",
                                                                                                                alt="Target User",
                                                                                                            )
                                                                                                        ],
                                                                                                    )
                                                                                                ],
                                                                                            ),
                                                                                            html.Div(
                                                                                                className="col-sm-9 col-md-9",
                                                                                                children=[
                                                                                                    html.Div(
                                                                                                        className="card-body right-bg-blue h-100",
                                                                                                        id="money-moved-card",
                                                                                                        children=[
                                                                                                            
                                                                                                        ],
                                                                                                    )
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                    )
                                                                                ],
                                                                            )
                                                                        ],
                                                                    ),
                                                                ],
                                                            ),
                                                            html.Div(
                                                                className="col-xxl-12 col-lg-12 col-md-12 order-1 mt-1 mb-6",
                                                                children=[
                                                                    html.Div(
                                                                        className="row",
                                                                        children=[
                                                                            html.Div(
                                                                                className="col-lg-4 col-md-4",
                                                                                children=[
                                                                                    html.Div(
                                                                                        className="card h-100",
                                                                                        children=[
                                                                                            html.Div(
                                                                                                className="card-body",
                                                                                                children=[
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
                                                                                                        value=unique_fy[
                                                                                                            0
                                                                                                        ],
                                                                                                        clearable=False,
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            html.Div(
                                                                                className="col-lg-4 col-md-4 ",
                                                                                children=[
                                                                                    html.Div(
                                                                                        className="card h-100",
                                                                                        children=[
                                                                                            html.Div(
                                                                                                className="card-body ",
                                                                                                children=[
                                                                                                    html.Span(
                                                                                                        "Select Payment Platform",
                                                                                                        className="d-block fw-medium mb-1",
                                                                                                    ),
                                                                                                    dcc.Dropdown(
                                                                                                        id="payment-platform-filter",
                                                                                                        options=[
                                                                                                            dict(
                                                                                                                label=platform,
                                                                                                                value=platform,
                                                                                                            )
                                                                                                            for platform in unique_platforms
                                                                                                        ],
                                                                                                        placeholder="Payment Platform",
                                                                                                        multi=True,
                                                                                                        # value=unique_fy[0],
                                                                                                        clearable=True,
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            html.Div(
                                                                                className="col-lg-4 col-md-4 ",
                                                                                children=[
                                                                                    html.Div(
                                                                                        className="card h-100",
                                                                                        children=[
                                                                                            html.Div(
                                                                                                className="card-body",
                                                                                                children=[
                                                                                                    html.Span(
                                                                                                        "Select Source (Chapter Types)",
                                                                                                        className="d-block fw-medium mb-1",
                                                                                                    ),
                                                                                                    dcc.Dropdown(
                                                                                                        id="chapter-type-filter",
                                                                                                        options=[
                                                                                                            dict(
                                                                                                                label=chapter,
                                                                                                                value=chapter,
                                                                                                            )
                                                                                                            for chapter in unique_chapter_types
                                                                                                        ],
                                                                                                        placeholder="Source (Chapter Types)",
                                                                                                        multi=True,
                                                                                                        # value=unique_fy[0],
                                                                                                        clearable=True,
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
                                                            ),
                                                            # -- End of Filters --
                                                            # -- KPI Cards --
                                                          
                                                            # html.Div(
                                                            #     children=[
                                                            #         html.Div(
                                                            #             id="money-moved-card",
                                                            #             style={
                                                            #                 "backgroundColor": colors[
                                                            #                     "highlight"
                                                            #                 ],
                                                            #                 "borderRadius": "10px",
                                                            #                 "marginBottom": "20px",
                                                            #                 "padding": "15px",
                                                            # #                 "boxShadow": "0 0 20px rgba(0, 0, 0, 0.15)",
                                                            #             },
                                                            #         ),
                                                            #         html.Div(
                                                            #             id="cf-money-moved-card",
                                                            #             style={
                                                            #                 "backgroundColor": colors[
                                                            #                     "highlight"
                                                            #                 ],
                                                            #                 "borderRadius": "10px",
                                                            #                 "marginBottom": "20px",
                                                            #                 "padding": "15px",
                                                            # #                 "boxShadow": "0 0 20px rgba(0, 0, 0, 0.15)",
                                                            #             },
                                                            #         ),
                                                            #         html.Div(
                                                            #             id = "cf-money-moved-card",
                                                            #             style={
                                                            #                 "backgroundColor": colors[
                                                            #                     "highlight"
                                                            #                 ],
                                                            #                 "borderRadius": "10px",
                                                            #                 "marginBottom": "20px",
                                                            #                 "padding": "15px",
                                                            # #                 "boxShadow": "0 0 20px rgba(0, 0, 0, 0.15)",
                                                            #             }
                                                            #         ),
                                                            #     ],
                                                            #     style={
                                                            #         "display": "flex",
                                                            #         # 'justifyContent': 'center',
                                                            #         "gap": "20px",  # adds space between cards
                                                            #         "flexWrap": "wrap",  # allows wrapping on smaller screens
                                                            #     },
                                                            # ),
                                                            # -- End of KPI Cards --
                                                            # -- Graphs --
                                                            html.Div(
                                                                className="row gy-4 mb-5",
                                                                children=[
                                                                    html.Div(
                                                                        className="col-xxl-6 col-md-6 col-xs-12 col-sm-12 col-xl-12 ",
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
                                                                                                                className="avatar-initial rounded-2 bg-label-danger",
                                                                                                                children=[
                                                                                                                    html.I(
                                                                                                                        className="bx bx-trending-up bx-lg text-danger"
                                                                                                                    )
                                                                                                                ],
                                                                                                            )
                                                                                                        ],
                                                                                                    ),
                                                                                                    # html.Div(
                                                                                                    #     children=[
                                                                                                    #         html.H6(
                                                                                                    #             "Money Moved Monthly (Cumulative)",
                                                                                                    #             className="text-lg mb-3 ml-1",
                                                                                                    #         ),
                                                                                                    #         html.Span(
                                                                                                    #             html.I(className="bi bi-magic", id="ai-icon",
                                                                                                    #                 style={"cursor": "pointer", "float": "right", "fontSize": "1.2rem", "marginLeft": "10px"}),
                                                                                                    #         ),
                                                                                                    #         dbc.Tooltip("Click here for Actionable Insights (AI)",
                                                                                                    #                     target="ai-icon", placement="left"),
                                                                                                    #     ],
                                                                                                    # ),
                                                                                                    chart_header_title_with_ai(
                                                                                                        title="Money Moved Monthly (Cumulative)",
                                                                                                        chart_id="money-moved-cumulative-graph",
                                                                                                    ),
                                                                                                    # html.Div([
                                                                                                    #     dbc.Row([
                                                                                                    #         dbc.Col(
                                                                                                    #             html.H6("Money Moved Monthly (Cumulative)", className="mb-0"),
                                                                                                    #             width="auto"
                                                                                                    #         ),
                                                                                                    #         dbc.Col(
                                                                                                    #             html.Div(
                                                                                                    #                 html.I(className="bi bi-magic", id="ai-icon", style={
                                                                                                    #                     "cursor": "pointer",
                                                                                                    #                     "fontSize": "1.3rem",
                                                                                                    #                     "color": "#065A60"
                                                                                                    #                 }),
                                                                                                    #                 style={"textAlign": "right"}
                                                                                                    #             ),
                                                                                                    #             width="auto"
                                                                                                    #         ),
                                                                                                    #     ],
                                                                                                    #     justify="between",
                                                                                                    #     align="center",
                                                                                                    #     className="mb-2"
                                                                                                    #     ),
                                                                                                    #     dbc.Tooltip("Click here for Actionable Insights (AI)", target="ai-icon", placement="left")
                                                                                                    # ]),
                                                                                                ],
                                                                                            ),
                                                                                            html.Div(
                                                                                                className="table bordered-table mb-0 dataTable",
                                                                                                children=[
                                                                                                    dcc.Graph(
                                                                                                        id="money-moved-cumulative-graph",
                                                                                                        style={
                                                                                                            "backgroundColor": colors[
                                                                                                                "white"
                                                                                                            ],
                                                                                                            "borderRadius": "10px",
                                                                                                            "padding": "15px",
                                                                                                            # # "boxShadow": "0 0 20px rgba(0, 0, 0, 0.15)",
                                                                                                        },
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
                                                                        className="col-xxl-6 col-md-6 col-xs-12 col-sm-12 col-xl-12 ",
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
                                                                                                                className="avatar-initial rounded-2 bg-label-danger",
                                                                                                                children=[
                                                                                                                    html.I(
                                                                                                                        className="bx bx-trending-up bx-lg text-danger"
                                                                                                                    )
                                                                                                                ],
                                                                                                            )
                                                                                                        ],
                                                                                                    ),
                                                                                                    chart_header_title_with_ai(
                                                                                                        title="Counterfactual Money Moved Monthly (Cumulative)",
                                                                                                        chart_id="cf-money-moved-cumulative-graph",
                                                                                                    ),
                                                                                                    # html.Div(
                                                                                                    #     children=[
                                                                                                    #         html.H6(
                                                                                                    #             "Counterfactual Money Moved Monthly (Cumulative)",
                                                                                                    #             className="text-lg mb-3 ml-1",
                                                                                                    #         ),
                                                                                                    #     ],
                                                                                                    # ),
                                                                                                ],
                                                                                            ),
                                                                                            html.Div(
                                                                                                className="table bordered-table mb-0 dataTable",
                                                                                                children=[
                                                                                                    dcc.Graph(
                                                                                                        id="cf-money-moved-cumulative-graph",
                                                                                                        style={
                                                                                                            "backgroundColor": colors[
                                                                                                                "white"
                                                                                                            ],
                                                                                                            "borderRadius": "10px",
                                                                                                            "padding": "15px",
                                                                                                            # "boxShadow": "0 0 20px rgba(0, 0, 0, 0.15)",
                                                                                                        },
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
                                                            ),
                                                            html.Div(
                                                                className="row gy-4 mb-5",
                                                                children=[
                                                                    # html.Div(
                                                                    #     className="col-xxl-6 col-md-6 col-xs-12 col-sm-12 col-xl-12 ",
                                                                    #     children=[
                                                                    #         html.Div(
                                                                    #             className="card h-100",
                                                                    #             children=[
                                                                    #                 html.Div(
                                                                    #                     className="card-body",
                                                                    #                     children=[
                                                                    #                         html.Div(
                                                                    #                             className="card-title d-flex align-items-center mb-4",
                                                                    #                             children=[
                                                                    #                                 html.Div(
                                                                    #                                     className="avatar me-2",
                                                                    #                                     children=[
                                                                    #                                         html.Span(
                                                                    #                                             className="avatar-initial rounded-2 bg-label-danger",
                                                                    #                                             children=[
                                                                    #                                                 html.I(
                                                                    #                                                     className="bx bx-trending-up bx-lg text-danger"
                                                                    #                                                 )
                                                                    #                                             ],
                                                                    #                                         )
                                                                    #                                     ],
                                                                    #                                 ),
                                                                    #                                 html.Div(
                                                                    #                                     children=[
                                                                    #                                         html.H6(
                                                                    #                                             "Money Moved Monthly",
                                                                    #                                             className="text-lg mb-3 ml-1",
                                                                    #                                         ),
                                                                    #                                     ],
                                                                    #                                 ),
                                                                    #                             ],
                                                                    #                         ),
                                                                    #                         html.Div(
                                                                    #                             className="table bordered-table mb-0 dataTable",
                                                                    #                             children=[
                                                                    #                                 dcc.Graph(
                                                                    #                                     id = "money-moved-mosaic-graph",
                                                                    #                                     style = {
                                                                    #                                         'backgroundColor': colors['white'],
                                                                    #                                         'borderRadius': '10px',
                                                                    #                                         'padding': '15px',
                                                                    #                                         'boxShadow': '0 0 20px rgba(0, 0, 0, 0.15)'
                                                                    #                                     }
                                                                    #                                 ),
                                                                    #                             ],
                                                                    #                         ),
                                                                    #                     ],
                                                                    #                 ),
                                                                    #             ],
                                                                    #         ),
                                                                    #     ],
                                                                    # ),
                                                                    html.Div(
                                                                        className="col-xxl-6 col-md-6 col-xs-12 col-sm-12 col-xl-12 ",
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
                                                                                                                className="avatar-initial rounded-2 bg-label-danger",
                                                                                                                children=[
                                                                                                                    html.I(
                                                                                                                        className="bx bx-trending-up bx-lg text-danger"
                                                                                                                    )
                                                                                                                ],
                                                                                                            )
                                                                                                        ],
                                                                                                    ),
                                                                                                    chart_header_title_with_ai(
                                                                                                        title="Money Moved Monthly Trend",
                                                                                                        chart_id="money-moved-line-graph",
                                                                                                    ),
                                                                                                    #  html.Div(
                                                                                                    #      children=[
                                                                                                    #          html.H6(
                                                                                                    #              "Money Moved Monthly Trend",
                                                                                                    #              className="text-lg mb-3 ml-1",
                                                                                                    #          ),
                                                                                                    #      ],
                                                                                                    #  ),
                                                                                                    # TODO: adjust the header properly
                                                                                                ],
                                                                                            ),
                                                                                            html.Div(
                                                                                                className="row",  # Add a row wrapper for proper Bootstrap grid behavior
                                                                                                children=[
                                                                                                    html.Div(
                                                                                                        className="col-md-6 col-12",  # Half width on md and full on smaller screens
                                                                                                        children=[
                                                                                                            dbc.RadioItems(
                                                                                                                options=[
                                                                                                                    {
                                                                                                                        "label": "Actual MM",
                                                                                                                        "value": "payment_amount_usd",
                                                                                                                    },
                                                                                                                    {
                                                                                                                        "label": "Counterfactual MM",
                                                                                                                        "value": "payment_cf_amount_usd",
                                                                                                                    },
                                                                                                                ],
                                                                                                                value="payment_amount_usd",
                                                                                                                id="mm-cf-radio-filter",
                                                                                                                inline=True,
                                                                                                            )
                                                                                                        ],
                                                                                                    ),
                                                                                                    html.Div(
                                                                                                        className="col-md-6 col-12",  # Half width on md and full on smaller screens
                                                                                                        children=[
                                                                                                            dcc.Dropdown(
                                                                                                                id="line-drilldown-by-filter",
                                                                                                                options=[
                                                                                                                    dict(
                                                                                                                        label=item[
                                                                                                                            "label"
                                                                                                                        ],
                                                                                                                        value=item[
                                                                                                                            "value"
                                                                                                                        ],
                                                                                                                    )
                                                                                                                    for item in drilldown_by
                                                                                                                ],
                                                                                                                placeholder="Drilldown by",
                                                                                                                multi=False,
                                                                                                                value="",
                                                                                                                clearable=True,
                                                                                                            )
                                                                                                        ],
                                                                                                        style={
                                                                                                            "minWidth": "250px"
                                                                                                        },  # Optional: Prevents dropdown from shrinking too much
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            html.Div(
                                                                                                className="table bordered-table mb-0 dataTable",
                                                                                                children=[
                                                                                                    dcc.Graph(
                                                                                                        id="money-moved-line-graph",
                                                                                                        style={
                                                                                                            "backgroundColor": colors[
                                                                                                                "white"
                                                                                                            ],
                                                                                                            "borderRadius": "10px",
                                                                                                            "padding": "15px",
                                                                                                            # "boxShadow": "0 0 20px rgba(0, 0, 0, 0.15)",
                                                                                                        },
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
                                                                        className="col-xxl-6 col-md-6 col-xs-12 col-sm-12 col-xl-12 ",
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
                                                                                                                className="avatar-initial rounded-2 bg-label-danger",
                                                                                                                children=[
                                                                                                                    html.I(
                                                                                                                        className="bx bx-trending-up bx-lg text-danger"
                                                                                                                    )
                                                                                                                ],
                                                                                                            )
                                                                                                        ],
                                                                                                    ),
                                                                                                    chart_header_title_with_ai(
                                                                                                        title="Contribution by Day of the Week",
                                                                                                        chart_id="money-moved-heatmap-graph",
                                                                                                    ),
                                                                                                    # html.Div(
                                                                                                    #     children=[
                                                                                                    #         html.H6(
                                                                                                    #             "Contribution by Day of the Week",
                                                                                                    #             className="text-lg mb-3 ml-1",
                                                                                                    #         ),
                                                                                                    #     ],
                                                                                                    # ),
                                                                                                ],
                                                                                            ),
                                                                                            html.Div(
                                                                                                className="table bordered-table mb-0 dataTable",
                                                                                                children=[
                                                                                                    dcc.Graph(
                                                                                                        id="money-moved-heatmap-graph",
                                                                                                        style={
                                                                                                            "backgroundColor": colors[
                                                                                                                "white"
                                                                                                            ],
                                                                                                            "borderRadius": "10px",
                                                                                                            "padding": "15px",
                                                                                                            # "boxShadow": "0 0 20px rgba(0, 0, 0, 0.15)",
                                                                                                        },
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
                                                            ),
                                                            # Floating Draggable AI Panel
                                                            html.Div(
                                                                [
                                                                    dash_draggable.GridLayout(
                                                                        id="ai-draggable",
                                                                        children=[
                                                                            html.Div(
                                                                                [
                                                                                    html.Div(
                                                                                        "🧠 AI Insights",
                                                                                        style={
                                                                                            "fontWeight": "bold"
                                                                                        },
                                                                                    ),
                                                                                    html.Hr(),
                                                                                    html.Div(
                                                                                        id="ai-output",
                                                                                        style={
                                                                                            "overflowY": "auto",
                                                                                        },
                                                                                    ),
                                                                                    dcc.Loading(
                                                                                        id="ai-loading",
                                                                                        type="default",  # or "dot", "circle"
                                                                                        children=html.Div(
                                                                                            id="ai-output"
                                                                                        ),
                                                                                    ),
                                                                                ],
                                                                                style={
                                                                                    "backgroundColor": "white",
                                                                                    "padding": "15px",
                                                                                    "border": "1px solid #ccc",
                                                                                    "borderRadius": "8px",
                                                                                    "boxShadow": "2px 2px 10px rgba(0,0,0,0.1)",
                                                                                    "height": "100%",
                                                                                    "width": "100%",
                                                                                    "display": "flex",
                                                                                    "flexDirection": "column",
                                                                                    "flexGrow": "0",
                                                                                },
                                                                            )
                                                                        ],
                                                                        layout=[
                                                                            {
                                                                                "i": "0",
                                                                                "x": 0,
                                                                                "y": 0,
                                                                                "w": 100,
                                                                                "h": 10,
                                                                                "static": False,
                                                                            }
                                                                        ],
                                                                        # cols=12,
                                                                        # rowHeight=30,
                                                                        # width=100%,
                                                                        isDraggable=True,
                                                                        isResizable=True,
                                                                    )
                                                                ],
                                                            ),
                                                            dcc.Store(
                                                                id="ai-message-store",
                                                                data=[],
                                                            ),
                                                        ],
                                                    ),
                                                
                                                    html.Div(
                                                [
                                                    html.Footer(
                                                        className="content-footer footer bg-footer-theme",
                                                        children=[
                                                            html.Div(
                                                                className="container-fluid",
                                                                children=[
                                                                    html.Div(
                                                                        className="footer-container d-flex align-items-center justify-content-center py-4 flex-md-row flex-column",
                                                                        children=[
                                                                            html.Div(
                                                                                className="text-body txt-white",
                                                                                children=[
                                                                                    "© 2025. All rights reserved.",
                                                                                ],
                                                                            ),
                                                                        ],
                                                                    )
                                                                ],
                                                            )
                                                        ],
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
                    ),
                ],
            ),
        ]
    )
