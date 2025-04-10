import plotly.express as px
import plotly.graph_objects as go

from dash import html
import dash_ag_grid as dag
import dash_bootstrap_components as dbc

class Figure:

    plotly_template = "plotly_white"
    chart_margin = dict(l = 10, r = 10, t = 10, b = 10)

    def __init__(self):
        pass

    def create_goal_target_gauge_graph(self, value, goal):
        """
        """
        fig = go.Figure(
            go.Indicator(
                mode = "gauge+number+delta",
                value = value,
                number = dict(prefix = "$", valueformat = ",.0f"),
                delta = dict(
                    reference = goal,
                    position = "top",
                    increasing = dict(color = "green"),
                    decreasing = dict(color = "red")
                ),
                title = dict(text = "Money Moved YTD", font = dict(size = 24)),
                gauge = dict(
                    axis = dict(range = [0, goal], tickformat = "$,.0f"),
                    bar = dict(color = "darkblue"),
                    steps = [
                        dict(range = [0, goal * 0.5], color = "lightcoral"),
                        dict(range = [goal * 0.5, goal * 0.9], color = "gold"),
                        dict(range = [goal * 0.9, goal], color = "lightgreen")
                    ],
                    threshold = dict(
                        line = dict(color = "black", width = 4),
                        thickness = 0.75,
                        value = goal
                    )
                )
            )
        )

        return fig
    
    def create_title_card(self, body_text, header_text = None, footer_text = None, card_width = "18rem"):
        """
        Create a title card.

        Parameters:
        header_text: The header text.
        body_text: The body text.

        Returns:
        A title card.
        """

        return html.Div([
            dbc.Card([
                dbc.CardHeader(header_text, className = "card-title fw-bold") if header_text else None,
                dbc.CardBody([
                    html.H2(body_text, className = "card-text fw-bold"),
                ]),
                dbc.CardFooter(footer_text) if footer_text else None
            ], style = dict(width = card_width, flex = 1),), 
        ])