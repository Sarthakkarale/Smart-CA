"""
=========================================================
Smart CA Dashboard
Charts
=========================================================
"""

import plotly.graph_objects as go
import streamlit as st


def _cash_flow_chart():
    """
    Monthly Cash Flow Chart
    """

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

    income = [60000, 64000, 62000, 68000, 71000, 75000]

    expenses = [28000, 30000, 27000, 32000, 29500, 28500]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=months,
            y=income,
            mode="lines+markers",
            name="Income",
            line=dict(width=4),
        )
    )

    fig.add_trace(
        go.Scatter(
            x=months,
            y=expenses,
            mode="lines+markers",
            name="Expenses",
            line=dict(width=4),
        )
    )

    fig.update_layout(

        title="Cash Flow",

        height=360,

        template="plotly_white",

        margin=dict(l=10, r=10, t=50, b=10),

        legend=dict(
            orientation="h",
            y=1.08,
        ),

        xaxis_title="",

        yaxis_title="Amount (₹)",

    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


def _savings_chart():
    """
    Savings Trend
    """

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

    savings = [32000, 34000, 35000, 39000, 42000, 46550]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=months,
            y=savings,
            name="Savings",
        )
    )

    fig.update_layout(

        title="Savings Trend",

        height=360,

        template="plotly_white",

        margin=dict(l=10, r=10, t=50, b=10),

        xaxis_title="",

        yaxis_title="Amount (₹)",

    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )


def render_charts():
    """
    Dashboard Charts Section
    """

    left, right = st.columns(2)

    with left:

        _cash_flow_chart()

    with right:

        _savings_chart()