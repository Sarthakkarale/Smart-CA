"""
=========================================================
Smart CA Dashboard
Profile Summary
=========================================================
"""

import streamlit as st


def _progress_card(
    title: str,
    value: int,
    color: str = "#6D5EF8",
):
    """
    Render progress indicator.
    """

    st.markdown(f"**{title}**")

    st.progress(value)

    st.caption(f"{value}% Completed")

    st.write("")


def render_profile_summary():
    """
    Render Profile Summary Panel.
    """

    st.subheader("👤 Profile Summary")

    st.write("")

    # -----------------------------------------------------
    # USER CARD
    # -----------------------------------------------------

    st.markdown(
        """
        <div style="
            background:white;
            padding:24px;
            border-radius:20px;
            text-align:center;
            box-shadow:0 12px 30px rgba(0,0,0,.08);
            margin-bottom:20px;
        ">

        <div style="
            width:90px;
            height:90px;
            margin:auto;
            border-radius:50%;
            background:#6D5EF8;
            color:white;
            display:flex;
            justify-content:center;
            align-items:center;
            font-size:34px;
            font-weight:bold;
        ">
            S
        </div>

        <h3 style="margin-top:18px;">
            Sarthak
        </h3>

        <p style="color:#64748B;">
            Premium Member
        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # -----------------------------------------------------
    # PROFILE COMPLETION
    # -----------------------------------------------------

    st.markdown("### 📋 Profile Completion")

    _progress_card(
        "Financial Profile",
        80,
    )

    _progress_card(
        "KYC Verification",
        100,
    )

    _progress_card(
        "Document Upload",
        65,
    )

    st.divider()

    # -----------------------------------------------------
    # FINANCIAL HEALTH
    # -----------------------------------------------------

    st.markdown("### ❤️ Financial Health")

    st.metric(
        label="Health Score",
        value="82 / 100",
        delta="+5",
    )

    st.success(
        "Excellent! You're maintaining healthy savings habits."
    )

    st.divider()

    # -----------------------------------------------------
    # MONTHLY GOAL
    # -----------------------------------------------------

    st.markdown("### 🎯 Monthly Goal")

    st.progress(72)

    st.caption("₹36,000 of ₹50,000 saved")

    st.write("")

    # -----------------------------------------------------
    # QUICK ACTIONS
    # -----------------------------------------------------

    st.markdown("### ⚡ Quick Actions")

    if st.button(
        "✏️ Edit Profile",
        use_container_width=True,
        key="edit_profile_btn",
    ):
        st.info("Profile page integration in Sprint 2.")

    if st.button(
        "📂 Upload Documents",
        use_container_width=True,
        key="upload_docs_btn",
    ):
        st.info("Documents module coming soon.")

    if st.button(
        "📈 View Reports",
        use_container_width=True,
        key="view_reports_btn",
    ):
        st.info("Reports module coming soon.")

    st.write("")

    st.caption(
        "Last Updated: Today"
    )