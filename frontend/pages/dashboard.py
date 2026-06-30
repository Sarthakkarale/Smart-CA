import streamlit as st

from services.dashboard_service import DashboardService
from components.metric_card import metric_card


def calculate_health(profile):

    score = 100

    if profile["monthly_expenses"] > profile["monthly_income"] * 0.8:
        score -= 20

    if profile["debt_amount"] > profile["annual_income"]:
        score -= 20

    if profile["existing_savings"] < profile["monthly_income"] * 6:
        score -= 15

    if profile["existing_investments"] == 0:
        score -= 15

    return max(score, 0)


def show_dashboard():

    token = st.session_state.access_token

    response = DashboardService.get_profile(token)

    if response.status_code != 200:

        st.warning(
            "Please complete your financial profile first."
        )

        if st.button("Complete Profile"):

            st.session_state.page = "Financial Profile"

            st.rerun()

        return

    profile = response.json()

    score = calculate_health(profile)

    st.markdown(
        f"""
        <div class="page-title">
            Welcome 👋
        </div>

        <div class="page-subtitle">
            Financial Health Score : <b>{score}/100</b>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        metric_card(
            "Monthly Income",
            f"₹ {profile['monthly_income']:,.0f}",
            "💰"
        )

    with c2:

        metric_card(
            "Expenses",
            f"₹ {profile['monthly_expenses']:,.0f}",
            "💸"
        )

    with c3:

        savings = (
            profile["monthly_income"]
            - profile["monthly_expenses"]
        )

        metric_card(
            "Savings",
            f"₹ {savings:,.0f}",
            "🏦"
        )

    with c4:

        metric_card(
            "Debt",
            f"₹ {profile['debt_amount']:,.0f}",
            "📉"
        )

    st.write("")

    st.subheader("🤖 AI Suggestions")

    if profile["existing_savings"] < profile["monthly_income"] * 6:

        st.info(
            "Increase your emergency fund to at least 6 months of expenses."
        )

    if profile["existing_investments"] < profile["annual_income"] * 0.5:

        st.info(
            "Consider increasing long-term investments."
        )

    if profile["debt_amount"] > profile["annual_income"]:

        st.warning(
            "Your debt is high compared to your annual income."
        )

    st.write("")

    st.subheader("🎯 Financial Goals")

    st.success(profile["financial_goals"])

