"""
=========================================================
Smart CA
Create Financial Profile
=========================================================
"""

import streamlit as st

from components.wizard import (
    get_current_step,
    next_step,
    previous_step,
    render_navigation,
    render_step_title,
    render_submit_button,
    render_completion,
    render_wizard_header,
)


# ==========================================================
# STEP 1
# ==========================================================

def render_personal_information():
    """
    Step 1
    """

    render_step_title(
        "Personal Information",
        "Tell us about yourself."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.text_input(
            "First Name",
            key="first_name",
        )

        st.text_input(
            "Email Address",
            key="email",
        )

        st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            key="age",
        )

        st.selectbox(
            "Occupation",
            [
                "Salaried",
                "Business",
                "Freelancer",
                "Student",
                "Retired",
            ],
            key="occupation",
        )

    with col2:

        st.text_input(
            "Last Name",
            key="last_name",
        )

        st.text_input(
            "Mobile Number",
            key="mobile",
        )

        st.selectbox(
            "Gender",
            [
                "Male",
                "Female",
                "Other",
            ],
            key="gender",
        )

        st.selectbox(
            "Marital Status",
            [
                "Single",
                "Married",
            ],
            key="marital_status",
        )

    previous_clicked, next_clicked = render_navigation(
        show_previous=False
    )

    if next_clicked:

        next_step()

        st.rerun()
# ==========================================================
# STEP 2
# ==========================================================

def render_financial_information():
    """
    Step 2
    """

    render_step_title(
        "Financial Information",
        "Help us understand your financial position."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.number_input(
            "Monthly Income (₹)",
            min_value=0,
            step=1000,
            key="monthly_income",
        )

        st.number_input(
            "Monthly Expenses (₹)",
            min_value=0,
            step=1000,
            key="monthly_expenses",
        )

        st.number_input(
            "Monthly Savings (₹)",
            min_value=0,
            step=1000,
            key="monthly_savings",
        )

        st.number_input(
            "Bank Balance (₹)",
            min_value=0,
            step=1000,
            key="bank_balance",
        )

    with col2:

        st.number_input(
            "Investment Value (₹)",
            min_value=0,
            step=1000,
            key="investment_value",
        )

        st.number_input(
            "Loan Amount (₹)",
            min_value=0,
            step=1000,
            key="loan_amount",
        )

        st.number_input(
            "Insurance Cover (₹)",
            min_value=0,
            step=1000,
            key="insurance_cover",
        )

        st.selectbox(
            "Primary Income Source",
            [
                "Salary",
                "Business",
                "Freelancing",
                "Rental Income",
                "Other",
            ],
            key="income_source",
        )

    previous_clicked, next_clicked = render_navigation()

    if previous_clicked:

        previous_step()

        st.rerun()

    if next_clicked:

        next_step()

        st.rerun()
# ==========================================================
# STEP 3
# ==========================================================

def render_financial_goals():
    """
    Step 3
    """

    render_step_title(
        "Financial Goals",
        "Tell us what you want to achieve."
    )

    st.subheader("🎯 Goals")

    col1, col2 = st.columns(2)

    with col1:

        emergency_fund = st.checkbox(
            "Build Emergency Fund",
            key="goal_emergency",
        )

        retirement = st.checkbox(
            "Retirement Planning",
            key="goal_retirement",
        )

        child_education = st.checkbox(
            "Child Education",
            key="goal_child",
        )

        home_purchase = st.checkbox(
            "Purchase House",
            key="goal_house",
        )

    with col2:

        vehicle = st.checkbox(
            "Buy Vehicle",
            key="goal_vehicle",
        )

        vacation = st.checkbox(
            "International Vacation",
            key="goal_vacation",
        )

        wealth = st.checkbox(
            "Wealth Creation",
            key="goal_wealth",
        )

        debt_free = st.checkbox(
            "Become Debt Free",
            key="goal_debt",
        )

    st.write("")

    st.subheader("📈 Investment Preference")

    investment_preference = st.multiselect(
        "Preferred Investment Options",
        [
            "Fixed Deposit",
            "Mutual Funds",
            "Stocks",
            "Gold",
            "PPF",
            "NPS",
            "Real Estate",
            "Cryptocurrency",
        ],
        key="investment_preference",
    )

    st.write("")

    st.subheader("⚖ Risk Appetite")

    risk_appetite = st.radio(
        "Select your risk profile",
        [
            "Conservative",
            "Moderate",
            "Aggressive",
        ],
        horizontal=True,
        key="risk_profile",
    )

    st.write("")

    st.subheader("📅 Investment Horizon")

    investment_horizon = st.selectbox(
        "How long do you plan to invest?",
        [
            "Less than 1 Year",
            "1 - 3 Years",
            "3 - 5 Years",
            "5 - 10 Years",
            "More than 10 Years",
        ],
        key="investment_horizon",
    )

    previous_clicked, next_clicked = render_navigation()

    if previous_clicked:

        previous_step()

        st.rerun()

    if next_clicked:

        next_step()

        st.rerun()
# ==========================================================
# STEP 4
# ==========================================================

def render_review():
    """
    Step 4
    """

    render_step_title(
        "Review Your Financial Profile",
        "Verify your information before submitting."
    )

    st.success(
        "Please review all the information entered in previous steps."
    )

    st.write("")

    # -----------------------------------------------------
    # PERSONAL INFORMATION
    # -----------------------------------------------------

    with st.expander(
        "👤 Personal Information",
        expanded=True,
    ):

        left, right = st.columns(2)

        with left:

            st.write(
                f"**First Name:** {st.session_state.get('first_name', '')}"
            )

            st.write(
                f"**Email:** {st.session_state.get('email', '')}"
            )

            st.write(
                f"**Age:** {st.session_state.get('age', '')}"
            )

            st.write(
                f"**Occupation:** {st.session_state.get('occupation', '')}"
            )

        with right:

            st.write(
                f"**Last Name:** {st.session_state.get('last_name', '')}"
            )

            st.write(
                f"**Mobile:** {st.session_state.get('mobile', '')}"
            )

            st.write(
                f"**Gender:** {st.session_state.get('gender', '')}"
            )

            st.write(
                f"**Marital Status:** {st.session_state.get('marital_status', '')}"
            )

    # -----------------------------------------------------
    # FINANCIAL INFORMATION
    # -----------------------------------------------------

    with st.expander(
        "💰 Financial Information",
        expanded=True,
    ):

        st.write(
            f"**Monthly Income:** ₹ {st.session_state.get('monthly_income',0):,}"
        )

        st.write(
            f"**Monthly Expenses:** ₹ {st.session_state.get('monthly_expenses',0):,}"
        )

        st.write(
            f"**Monthly Savings:** ₹ {st.session_state.get('monthly_savings',0):,}"
        )

        st.write(
            f"**Bank Balance:** ₹ {st.session_state.get('bank_balance',0):,}"
        )

        st.write(
            f"**Investments:** ₹ {st.session_state.get('investment_value',0):,}"
        )

        st.write(
            f"**Loan Amount:** ₹ {st.session_state.get('loan_amount',0):,}"
        )

        st.write(
            f"**Insurance Cover:** ₹ {st.session_state.get('insurance_cover',0):,}"
        )

        st.write(
            f"**Income Source:** {st.session_state.get('income_source','')}"
        )

    # -----------------------------------------------------
    # GOALS
    # -----------------------------------------------------

    with st.expander(
        "🎯 Financial Goals",
        expanded=True,
    ):

        st.write(
            f"**Investment Preference:** {', '.join(st.session_state.get('investment_preference', []))}"
        )

        st.write(
            f"**Risk Profile:** {st.session_state.get('risk_profile','')}"
        )

        st.write(
            f"**Investment Horizon:** {st.session_state.get('investment_horizon','')}"
        )

    previous_clicked, _ = render_navigation(
        show_next=False
    )

    if previous_clicked:

        previous_step()

        st.rerun()

    if render_submit_button():

        # Sprint 1
        # Backend Integration in Sprint 2

        render_completion()

        st.balloons()


# ==========================================================
# PAGE
# ==========================================================

def render_page():
    """
    Financial Profile Wizard
    """

    render_wizard_header()

    step = get_current_step()

    if step == 1:

        render_personal_information()

    elif step == 2:

        render_financial_information()

    elif step == 3:

        render_financial_goals()

    elif step == 4:

        render_review()