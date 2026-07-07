"""
=========================================================
Smart CA Dashboard
Summary Cards
=========================================================
"""

import streamlit as st


def metric_card(
    title: str,
    value: str,
    change: str,
    emoji: str,
    positive: bool = True,
):
    """
    Reusable KPI Card
    """

    color = "#10B981" if positive else "#EF4444"

    st.markdown(
        f"""
        <div style="
            background:white;
            border-radius:20px;
            padding:22px;
            box-shadow:0 12px 30px rgba(0,0,0,.08);
            border:1px solid #E5E7EB;
            min-height:170px;
        ">

            <div style="
                display:flex;
                justify-content:space-between;
                align-items:center;
            ">

                <div style="
                    font-size:15px;
                    color:#64748B;
                    font-weight:600;
                ">
                    {title}
                </div>

                <div style="
                    font-size:30px;
                ">
                    {emoji}
                </div>

            </div>

            <div style="
                margin-top:18px;
                font-size:34px;
                font-weight:800;
                color:#111827;
            ">
                {value}
            </div>

            <div style="
                margin-top:14px;
                color:{color};
                font-size:14px;
                font-weight:700;
            ">
                {change}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


def render_summary_cards():
    """
    Dashboard KPI Section
    """

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        metric_card(
            title="Monthly Income",
            value="₹75,000",
            change="+8.5%",
            emoji="💰",
        )

    with col2:

        metric_card(
            title="Monthly Expenses",
            value="₹28,450",
            change="-3.2%",
            emoji="💸",
        )

    with col3:

        metric_card(
            title="Savings",
            value="₹46,550",
            change="+14.8%",
            emoji="🏦",
        )

    with col4:

        metric_card(
            title="Net Worth",
            value="₹18.5 L",
            change="+12.4%",
            emoji="📈",
        )