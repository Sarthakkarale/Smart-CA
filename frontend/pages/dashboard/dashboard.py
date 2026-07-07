"""
=========================================================
Smart CA Dashboard
=========================================================
"""

import streamlit as st

from pages.dashboard.summary import render_summary_cards
from pages.dashboard.charts import render_charts
from pages.dashboard.suggestions import render_ai_suggestions
from pages.dashboard.profile_summary import render_profile_summary


def render_page():
    """
    Dashboard UI
    """

    sidebar, content = st.columns([1.1, 4.9], gap="large")

    # =====================================================
    # SIDEBAR
    # =====================================================

    with sidebar:

        st.image(
            "assets/images/logo.png",
            width=70,
        )

        st.markdown("# Smart CA")

        st.caption("AI Financial Assistant")

        st.divider()

        menu = [
            "🏠 Dashboard",
            "👤 Profile",
            "📈 Investments",
            "🧾 Tax",
            "📊 Reports",
            "⚙️ Settings",
        ]

        for item in menu:
            st.button(
                item,
                use_container_width=True,
            )

        st.divider()

        st.info(
            """
Complete your Financial Profile
to unlock AI recommendations.
"""
        )

    # =====================================================
    # MAIN CONTENT
    # =====================================================

    with content:

        top_left, top_right = st.columns([3, 1])

        with top_left:

            st.title("Welcome Back 👋")

            st.caption(
                "Here's your financial overview."
            )

        with top_right:

            st.metric(
                "Today's Date",
                "02 Jul 2026",
            )

        st.write("")

        render_summary_cards()

        st.write("")

        render_charts()

        st.write("")

        bottom_left, bottom_right = st.columns([2, 1])

        with bottom_left:
            render_ai_suggestions()

        with bottom_right:
            render_profile_summary()