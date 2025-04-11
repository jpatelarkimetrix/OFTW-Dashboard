# X coordinates evenly spaced across the plot width.
    path_x = np.linspace(0, 10, num_points)
    # print(path_x)
    # # A gentle curve using sine for a pleasing visual.
    # path_y = 2 * np.sin(path_x / 2) + 5

    # start_y, end_y = 3, 8
    # path_y = np.linspace(start_y, end_y, num_points)  # strictly upward

    # Instead of a fixed upward slope, use cumulative donations to determine y elevation.
    # Define minimum and maximum y-level for the pathway.
    y_min, y_max = 3, 8
    # Normalize cumulative donation amounts relative to the target.
    cumulative_norm = cumulative_donations / fund_raise_target
    # Compute y values so that 0 donation maps to y_min and target maps to y_max.
    path_y = y_min + cumulative_norm * (y_max - y_min)
    # print(path_y)

    # Determine the last month with donation data (nonzero donation).
    non_zero_indices = np.nonzero(cumulative_donations)[0]
    current_idx = int(np.max(non_zero_indices)) if len(non_zero_indices) > 0 else 0

    # Plot the remaining unfilled path from the current month onward, if any.
    if current_idx < num_points - 1:
        fig.add_trace(go.Scatter(
            x = path_x[current_idx+1:],
            y = path_y[current_idx+1:],
            mode = 'lines',
            line = dict(color = 'rgba(200, 200, 200, 0.5)', width = 10),
            hoverinfo = 'none',
            showlegend = False
        ))

    # Plot the filled portion of the pathway.
    fig.add_trace(go.Scatter(
        x = path_x[:current_idx+1],
        y = path_y[:current_idx+1],
        mode = 'lines',
        line = dict(color = colors['primary'], width = 10),
        hoverinfo = 'none',
        showlegend = False
    ))

    # Define milestone values for the fiscal year
    milestones = [0.25, 0.5, 0.75, 1.0]
    milestone_values = [fund_raise_target * m for m in milestones]
    print(milestone_values)
    milestone_labels = [
        f"${int(fund_raise_target*0.25):,}",
        f"${int(fund_raise_target*0.5):,}",
        f"${int(fund_raise_target*0.75):,}",
        f"${fund_raise_target:,} Goal"
    ]

    # Place milestone markers on the curve.
    for val, label in zip(milestone_values, milestone_labels):
        # Find the month closest to the milestone value.
        closest_idx = np.argmin(np.abs(cumulative_donations - val))
        print(closest_idx)
        is_reached = cumulative_donations[closest_idx] >= val
        marker_color = colors['primary'] if is_reached else 'rgba(200, 200, 200, 0.7)'
        marker_size = 15 if is_reached else 12
        
        fig.add_trace(go.Scatter(
            x = [path_x[closest_idx]],
            y = [path_y[closest_idx]],
            mode = 'markers',
            marker = dict(
                color = marker_color,
                size = marker_size,
                line = dict(width = 2, color = 'white')
            ),
            hoverinfo = 'none',
            showlegend = False
        ))
        
        # Alternate the label vertical offsets for clarity.
        y_offset = 0.8 if milestone_values.index(val) % 2 == 0 else -0.8
        fig.add_annotation(
            x = path_x[closest_idx],
            y = path_y[closest_idx] + y_offset,
            text = label,
            showarrow = False,
            font = dict(color = colors['text'], size = 12)
        )

    # Mark the current position with a distinct marker.
    fig.add_trace(go.Scatter(
        x = [path_x[current_idx]],
        y = [path_y[current_idx]],
        mode = 'markers',
        marker = dict(
            color = 'white',
            size = 13,
            line = dict(width = 3, color = colors['primary'])
        ),
        hoverinfo = 'none',
        showlegend = False
    ))

    # Add an annotation with the current cumulative donation amount.
    fig.add_annotation(
        x = path_x[current_idx],
        y = path_y[current_idx] - 1.5,
        text = f"Current: ${cumulative_donations[current_idx]:,}",
        showarrow = False,
        font = dict(size = 14, color = colors['primary'])
    )

    # Annotate each month label along the path.
    for i, month in enumerate(months):
        fig.add_annotation(
            x = path_x[i],
            y = path_y[i] + 0.3,
            text = month,
            showarrow = False,
            font = dict(size = 11, color = "#444444")
        )

    # Add a note indicating data is only available until the current month.
    if current_idx < num_points - 1:
        fig.add_annotation(
            x = (path_x[0] + path_x[-1]) / 2,
            y = 1.2,  # Adjust this value as needed
            text = f"Data available up to {months[current_idx]}",
            showarrow = False,
            font = dict(size = 14, color = colors['text'])
        )

    # Final layout adjustments.
    fig.update_layout(
        title = dict(
            text = "Monthly Cumulative Donation Pathway (FY: Jul-Jun)",
            y = 0.95,
            x = 0.5,
            xanchor = 'center',
            yanchor = 'top'
        ),
        height = 600,
        plot_bgcolor = 'rgba(0,0,0,0)',
        paper_bgcolor = 'rgba(0,0,0,0)',
        xaxis = dict(
            range = [-1, 11],
            showgrid = False,
            zeroline = False,
            showticklabels = False
        ),
        yaxis = dict(
            range = [1, 9],
            showgrid = False,
            zeroline = False,
            showticklabels = False
        ),
        showlegend = False,
        margin = dict(l = 50, r = 50, t = 80, b = 50)
    )




###################


 # print(money_moved_path_df)

    # Cumulative sum to get path-like shape
    cumulative_donations = money_moved_path_df["money_moved_ytd"].to_numpy()
    # Pad with zeros to make the size 12 to match with # of months
    cumulative_donations = np.pad(cumulative_donations, (0, 12 - len(cumulative_donations)), 'constant')

    # Fiscal year months starting in July
    months = ["Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun"]    

    # Create figure
    fig = go.Figure()

    num_points = len(months)
    # X coordinates evenly spaced across the plot width.
    x_vals = money_moved_path_df["payment_date_calendar_monthyear"].to_numpy() # np.arange(num_points)  # [0, 1, 2, ..., 11]
   
    # Find index of last actual data month (non-zero donation)
    # If all zero, default to 0.
    nonzero_indices = np.nonzero(cumulative_donations)[0]
    current_idx = nonzero_indices[-1] if len(nonzero_indices) > 0 else 0

    #Extend a dashed horizontal line from current_idx to the end 
    #    so it doesn't drop to zero. 
    #    This is purely cosmetic — to show "no new data but same total".
    # if current_idx < num_points - 1:
    #     fig.add_trace(go.Scatter(
    #         x = [x_vals[current_idx], x_vals[-1]],  # from current month to Jun
    #         y = [cumulative_donations[current_idx], fund_raise_target],  # last known donation -> goal
    #         mode = "lines+text",
    #         line = dict(width=3, dash="dot", color="gray"),
    #         showlegend = False,
    #         name = "Target",
    #         # text = ["", f"${fund_raise_target:,.2f}"],
    #         textposition = "bottom right",
    #         textfont = dict(size=12, color="gray"),
    #     ))

    # Plot the filled portion of the pathway.
    fig.add_trace(go.Scatter(
        x = x_vals[:current_idx+1],
        y = cumulative_donations[:current_idx+1],
        mode = "lines+markers+text",
        line = dict(width=4, color=colors['primary']),
        marker = dict(size=8, color=colors['primary']),
        text = [f"${x:,.2f}" for x in cumulative_donations[:current_idx + 1]],
        textposition = "bottom right",
        hoverinfo = "text",
        hovertemplate = "Cumulative Donations: $%{text}",
        showlegend = False,
        name = "Cumulative Donations"
    ))

    # Mark the current position with a distinct marker.
    fig.add_trace(go.Scatter(
        x = [x_vals[current_idx]],
        y = [cumulative_donations[current_idx]],
        mode = 'markers',
        marker = dict(
            color = 'white',
            size = 13,
            line = dict(width = 3, color = colors['primary'])
        ),
        hoverinfo = 'none',
        showlegend = False
    ))

    # Customize axes, add month labels at the bottom
    fig.update_layout(
        title = dict(text=f"Monthly Cumulative Money Moved ({selected_fy})", x=0.5),
        xaxis = dict(
            range = [-0.5, 12-0.5],
            showgrid=False,
            zeroline=True,
            showticklabels=True
        ),
        yaxis = dict(
            # range = [0, max(fund_raise_target, np.max(cumulative_donations)) * 1.1],
            showgrid=False,
            zeroline=True,
            showticklabels=True
        ),
        plot_bgcolor = "white",
        # margin = dict(l=60, r=60, t=70, b=60),
    )