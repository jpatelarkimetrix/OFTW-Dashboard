import plotly.express as px
import plotly.graph_objects as go

from typing import Optional

from dash import html
import dash_ag_grid as dag
import dash_bootstrap_components as dbc

import math
import polars as pl

class Figure:

    plotly_template = "plotly_white"
    chart_margin = dict(l = 10, r = 10, t = 10, b = 10)
    
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

    def __init__(self):
        pass

    def create_line_trace(
        self,
        x_values,
        y_values, 
        markers_mode: str,
        marker_size = None,
        marker_color = None,
        text_values_list = None,
        text_position: str = "bottom right",
        name_for_legend: Optional[str] = None, 
        legend_group: Optional[str] = None,
        line_color: Optional[str] = None, 
        line_type: Optional[str] = None,
        line_shape: Optional[str] = None, 
        line_width: Optional[int] = 3, 
        custom_data = None,
        hover_template = None,
        hover_info = None,
    ) -> go.Scatter:
        """
        Create a line trace which need to be added in the figure.

        Parameters:
        x_col: The x-axis data.
        y_col: The y-axis data.
        name_for_legend (Optional[str]): The name for the legend.
        color (Optional[str]): The color of the line.
        line_type (Optional[str]): The type of the line (e.g., 'dash', 'dot').
        shape (Optional[str]): The shape of the line (e.g., 'linear', 'spline').
        custom_data (Optional[List]): Custom data to attach to each point.

        Returns:
        A line Trace.
        """
        trace = go.Scatter(
            x = x_values,
            y = y_values,
            mode = markers_mode,
            marker = dict(
                size = marker_size,
                color = marker_color,
            ),
            line = dict(
                color = line_color,
                dash = line_type,
                shape = line_shape,
                width = line_width,
            ),
            name = name_for_legend,
            legendgroup = legend_group,
            text = text_values_list,
            textposition = text_position,
            customdata = custom_data,
            hovertemplate = hover_template,
            hoverinfo = hover_info,
        )

        return trace

    def create_kpi_card(self, value, goal):
        return html.Div([
        html.H3(f"${value:,.2f}", 
                style={
                    'textAlign': 'center',
                    'color': self.colors['primary'],
                    'marginBottom': '5px',
                    'fontSize': '28px'
                }),
        html.P("Funds Raised", 
               style={
                   'textAlign': 'center',
                   'color': self.colors['text']
               }),
        html.P(f"of ${goal:,} goal ({value/goal:.1%})", 
               style={
                   'textAlign': 'center',
                   'color': self.colors['secondary'],
                   'fontSize': '14px'
               })
    ])

    def create_monthly_mm_graph(self, df, y_col_name, target):
        """
        """

        x_vals = df["payment_date_calendar_monthyear"].to_list()
        y_vals = df[y_col_name].to_list()

        current_idx = len(x_vals) - 1

        if len(x_vals) < 12:
            x_vals = x_vals + ["Mar'25", "Apr'25", "May'25", "Jun'25"]     #ISSUE: hardcoded
            y_vals = y_vals + [None] * (12 - len(y_vals)) # + [target]

        fig = go.Figure()

        fig.add_trace(
            self.create_line_trace(
                x_values = x_vals,
                y_values = y_vals,
                markers_mode = "lines+markers+text",
                marker_size = 10,
                marker_color = self.colors['primary'],
                text_values_list = [f"${val:,.2f}" if val is not None else "" for val in y_vals],
                text_position = "top left",
                name_for_legend = "Cumulative Donations",
                # legend_group = "Cumulative Donations",
                line_color = self.colors['primary'],
                line_width = 6,
                hover_template = "%{text}",
            )
        )

        # Mark the current position with a distinct marker.
        fig.add_trace(go.Scatter(
            x = [x_vals[current_idx]],
            y = [y_vals[current_idx]],
            mode = 'markers',
            marker = dict(
                color = 'white',
                size = 13,
                line = dict(width = 3, color = self.colors['primary'])
            ),
            hoverinfo = 'none',
            showlegend = False
        ))

        # Add dotted goal trend line: from last actual to final FY month (jun'25)
        last_actual_month = x_vals[current_idx]
        last_actual_value = y_vals[current_idx]
        goal_line_x = [last_actual_month, "Jun'25"]
        goal_line_y = [last_actual_value, target]

        fig.add_trace(
            self.create_line_trace(
                x_values=goal_line_x,
                y_values=goal_line_y,
                markers_mode="lines+markers+text",
                marker_size= 6,
                marker_color=self.colors['secondary'],
                text_values_list=[None, f"Target: ${target:,.2f}"],
                text_position="top left",
                name_for_legend="Target",
                line_color=self.colors['secondary'],
                line_type="dot",
                hover_info="none",
                # hover_template="Trend to Goal",
            )
        )

        # Add milestones
        milestones = [0.25, 0.5, 0.75]
        milestone_values = [target * m for m in milestones]

        for value, percent in zip(milestone_values, milestones):
            label = f"${value:,} ({percent:.0%}) Achieved" if value <= y_vals[current_idx] else f"${value:,} ({percent:.0%})"
            fig.add_hline(
                y = value,
                line = dict(
                    color = self.colors['secondary'],
                    dash = "dot",
                    width = 1,
                ),
                opacity = 0.5,
                annotation_text = label,
                annotation_position = "top right",
            )

        # To show trimmed values
        fig.update_traces(
            cliponaxis = False,
        )

        fig.update_layout(
            hovermode = "x unified",
            showlegend = False,
            template = self.plotly_template,
            margin =  dict(l = 50, r = 10, t = 10, b = 10),
            xaxis = dict(
                title = "Month",
                tickvals = x_vals,
                ticktext = x_vals,
                showgrid = False,
                zeroline = False,
                showline = True,
                ticks = "outside",
                tickcolor = self.colors['secondary'],
            ),
            yaxis = dict(
                # title = "Cumulative Donations",
                # range = [0, target * 1.2],
                # tickformat = "$,.0f",
                showgrid = False,
                zeroline = False,
                showline = False,
                showticklabels = False,
                # ticks = "outside",
                # tickcolor = self.colors['secondary'],
            ),
            # title = dict(
            #     text = f"Monthly Cumulative Money Moved",
            #     x = 0.5,
            #     font = dict(size = 24),
            # ),
        )

        return fig

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

        fig.update_layout(
            # margin = self.chart_margin,
            template = self.plotly_template,
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
    
    def create_money_mural_mosaic(self, df: pl.DataFrame):
        """
        Given a Polars DataFrame with columns:
        - 'payment_date_calendar_monthyear' (string, e.g. "Jul '24")
        - 'money_moved_monthly' (float)

        Returns a Plotly Figure in the 'Money Mural' mosaic style.
        """

        # -------------------------
        # 1. Select and Rename for Simplicity (Optional)
        # -------------------------
        # Ensure we have only the needed columns, with intuitive names
        df_mosaic = df.select([
            pl.col("payment_date_calendar_monthyear").alias("month_label"),
            pl.col("money_moved_monthly").alias("monthly_amount")
        ])

        # -------------------------
        # 2. Create Grid Coordinates
        # -------------------------
        # Suppose we want 4 columns for the mosaic:
        cols = 4
        n = df_mosaic.height  # number of months in your DF
        rows = math.ceil(n / cols)

        # Assign each month a (grid_x, grid_y) position
        # We'll place the first month in top-left, next across to the right, etc.
        x_coords = []
        y_coords = []
        for i in range(n):
            x_coords.append(i % cols)        # column index
            # We'll invert row index so the first row is at the top (max y)
            y_coords.append(rows - 1 - (i // cols))

        # Attach them back to df_pd
        df_mosaic = df_mosaic.with_columns([
            pl.lit(x_coords).alias("grid_x"),
            pl.lit(y_coords).alias("grid_y")
        ])

        # df_mosaic["grid_x"] = x_coords
        # df_mosaic["grid_y"] = y_coords

        # -------------------------
        # 3. Build the Mosaic Plotly Figure
        # -------------------------
        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=df_mosaic["grid_x"],
                y=df_mosaic["grid_y"],
                mode="markers+text",
                text=df_mosaic["month_label"],
                textposition="middle center",
                # The color of the tiles is based on the monthly amount
                marker=dict(
                    symbol="square",
                    size=100,  # fix a tile size; adjust if you want bigger/smaller squares
                    color=df_mosaic["monthly_amount"],
                    colorscale=px.colors.sequential.Peach,           #TODO: change to One for the World colors
                    colorbar=dict(title="Monthly<br>Amount"),
                    showscale=False,
                    line=dict(color="black", width=1)
                ),
                hovertemplate=(
                    "Month: %{text}<br>" +
                    "Monthly Amount: $%{marker.color:,.2f}<extra></extra>"
                ),
                name="MosaicTiles"
            )
        )

        # Remove grid lines, ticks, etc., for a clean “mosaic” look
        fig.update_layout(
            template=self.plotly_template,
            margin=self.chart_margin,
            xaxis=dict(
                showgrid=False,
                zeroline=False,
                showline=False,
                tickvals=[],
                ticktext=[],
                # side = "top",
            ),
            yaxis=dict(
                showgrid=False,
                zeroline=False,
                showline=False,
                tickvals=[],
                ticktext=[]
            ),
        )

        return fig