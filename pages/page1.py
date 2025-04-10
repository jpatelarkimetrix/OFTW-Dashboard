import dash
from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc

import polars as pl

import plotly.graph_objects as go

from utils.data_loader import data_loader
from utils.data_preparer import DataPreparer
from utils.figure import Figure

dash.register_page(__name__, path = '/')

data_preparer = DataPreparer()
figure_instance = Figure()

unique_fy = data_preparer.get_col_unique_values("merged", "payment_date_fy", sort_desc = True)

def layout(**kwargs):
    return html.Div(
        children = [
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
            html.Div(
                children = [
                   dcc.Graph(
                        id = "money-moved-gauge-graph",
                    )
                ]
            )
        ]
    )


@callback(
    Output("money-moved-gauge-graph", "figure"),
    Input("fy-filter", "value")
)
def update_kpis(selected_fy):
    filters = []

    if selected_fy:
        filters.append(("payment_date_fy", "==", selected_fy))

    merged_lf = data_preparer.filter_data("merged", filters)

    money_moved_lf = (merged_lf
                   .select(["payment_date_fy", "payment_date_fm", "payment_date_calendar_year", "payment_date_calendar_month", "pledge_status", "pledge_chapter_type", "payment_portfolio", "payment_platform", "payment_date", "payment_amount_usd", "payment_cf_amount_usd"])
                   .filter(~pl.col("payment_portfolio").is_in(["One for the World Discretionary Fund", "One for the World Operating Costs"]))
                   .sort("payment_date_fm")
                )
    
    money_moved_ytd_value = money_moved_lf.select(pl.col("payment_amount_usd").sum()).collect().item()
    goal = 1_800_000

    fig = figure_instance.create_goal_target_gauge_graph(money_moved_ytd_value, goal)

    return fig

