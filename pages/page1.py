import dash
from dash import Input, Output, callback

import polars as pl
import numpy as np
import plotly.graph_objects as go

from utils.data_loader import data_loader
from utils.data_preparer import DataPreparer
from utils.figure import Figure

from pages.layouts import page1_layout

dash.register_page(__name__, path = '/')

data_preparer = DataPreparer()
figure_instance = Figure()

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

def layout(**kwargs):
    return page1_layout()

@callback(
    Output("money-moved-card", "children"),
    Output("cf-money-moved-card", "children"),
    Output("money-moved-graph", "figure"),
    Output("cf-money-moved-graph", "figure"),
    Output("money-moved-mosaic-graph", "figure"),
    Input("fy-filter", "value"),
)
def update_kpis(selected_fy ):
    filters = []

    fund_raise_target = 1_800_000
    cf_fund_raise_target = 1_260_000

    if selected_fy:
        filters.append(("payment_date_fy", "==", selected_fy))

    merged_lf = data_preparer.filter_data("merged", filters)

    money_moved_lf = (merged_lf
                   .select(["payment_date_fy", "payment_date_fm", "payment_date_calendar_year", "payment_date_calendar_month", "payment_date_calendar_monthname", "payment_date_calendar_monthyear", "pledge_status", "pledge_chapter_type", "payment_portfolio", "payment_platform", "payment_date", "payment_amount_usd", "payment_cf_amount_usd"])
                   .filter(~pl.col("payment_portfolio").is_in(["One for the World Discretionary Fund", "One for the World Operating Costs"]))
                   .sort("payment_date_fm")
                )
    
    # mm FYTD
    money_moved_ytd_value = money_moved_lf.select(pl.col("payment_amount_usd").sum()).collect().item()
    mm_card = figure_instance.create_kpi_card(money_moved_ytd_value, goal = fund_raise_target)

    # cf mm FYTD
    cf_money_moved_ytd_value = money_moved_lf.select(pl.col("payment_cf_amount_usd").sum()).collect().item()
    cf_mm_card = figure_instance.create_kpi_card(cf_money_moved_ytd_value, goal = cf_fund_raise_target)

    # money moved monthly
    money_moved_ytd_df = (money_moved_lf
        .group_by(["payment_date_fm", "payment_date_calendar_year", "payment_date_calendar_month", "payment_date_calendar_monthyear"])
        .agg([
            pl.col("payment_amount_usd").sum().alias("money_moved_monthly"),
            pl.col("payment_cf_amount_usd").sum().alias("cf_money_moved_monthly"),
        ])
        .sort("payment_date_fm")
        .with_columns([
            pl.cum_sum("money_moved_monthly").alias("money_moved_cumulative"),
            pl.cum_sum("cf_money_moved_monthly").alias("cf_money_moved_cumulative"),
        ])
        .collect()
    )

    # print(money_moved_ytd_df)
 
    mm_monthly_fig = figure_instance.create_monthly_mm_graph(money_moved_ytd_df, "money_moved_cumulative", fund_raise_target)

    cf_mm_monthly_fig = figure_instance.create_monthly_mm_graph(money_moved_ytd_df, "cf_money_moved_cumulative", cf_fund_raise_target)

    fig = figure_instance.create_money_mural_mosaic(money_moved_ytd_df)

    return mm_card, cf_mm_card, mm_monthly_fig, cf_mm_monthly_fig, fig

