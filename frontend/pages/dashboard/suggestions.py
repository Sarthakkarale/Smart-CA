"""
=========================================================
Smart CA Dashboard
AI Suggestions
=========================================================
"""

import streamlit as st


def _suggestion_card(
    title: str,
    description: str,
    priority: str,
    icon: str,
    color: str,
):
    """
    Reusable AI suggestion card.
    """

    st.markdown(
        f"""
        <div style="
            background:white;
            border-radius:20px;
            padding:20px;
            margin-bottom:18px;
            border-left:6px solid {color};
            box-shadow:0 8px 24px rgba(0,0,0,.08);
        ">

            <div style="
                display:flex;
                justify-content:space-between;
                align-items:center;
            ">

                <div style="
                    font-size:24px;
                ">
                    {icon}
                </div>

                <span style="
                    background:{color};
                    color:white;
                    padding:6px 12px;
                    border-radius:20px;
                    font-size:12px;
                    font-weight:600;
                ">
                    {priority}
                </span>

            </div>

            <div style="
                margin-top:16px;
                font-size:18px;
                font-weight:700;
                color:#1E293B;
            ">
                {title}
            </div>

            <div style="
                margin-top:10px;
                color:#64748B;
                line-height:1.7;
                font-size:14px;
            ">
                {description}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


def render_ai_suggestions():
    """
    Render AI Suggestions section.
    """

    st.subheader("🤖 AI Recommendations")

    st.caption(
        "Personalized financial suggestions generated from your profile."
    )

    st.write("")

    _suggestion_card(
        title="Increase Monthly SIP",
        description=(
            "Increase your SIP investment by ₹2,000/month "
            "to potentially build a larger retirement corpus."
        ),
        priority="HIGH",
        icon="📈",
        color="#6D5EF8",
    )

    _suggestion_card(
        title="Tax Saving Opportunity",
        description=(
            "You still have approximately ₹48,000 available "
            "under Section 80C for this financial year."
        ),
        priority="MEDIUM",
        icon="🧾",
        color="#10B981",
    )

    _suggestion_card(
        title="Emergency Fund",
        description=(
            "Your emergency fund covers about 4 months of "
            "expenses. Consider increasing it to 6 months."
        ),
        priority="MEDIUM",
        icon="🛡️",
        color="#F59E0B",
    )

    _suggestion_card(
        title="Budget Alert",
        description=(
            "Entertainment spending increased by 18% this "
            "month compared to last month."
        ),
        priority="LOW",
        icon="💡",
        color="#EF4444",
    )