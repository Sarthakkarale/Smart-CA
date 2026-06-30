import streamlit as st
from services.profile_service import ProfileService


# ==========================================================
# Session Initialization
# ==========================================================

if "wizard_step" not in st.session_state:
    st.session_state.wizard_step = 1

if "profile_data" not in st.session_state:
    st.session_state.profile_data = {}


# ==========================================================
# Progress Bar
# ==========================================================

def show_progress(step):
    progress = step / 4

    st.progress(progress)

    cols = st.columns(4)

    titles = [
        "Personal",
        "Income",
        "Assets",
        "Goals"
    ]

    for i in range(4):

        if i + 1 == step:
            cols[i].markdown(
                f"""
                <div style="
                    text-align:center;
                    font-weight:700;
                    color:#6D5EF8;
                ">
                    {titles[i]}
                </div>
                """,
                unsafe_allow_html=True,
            )

        else:

            cols[i].markdown(
                f"""
                <div style="
                    text-align:center;
                    color:#64748B;
                ">
                    {titles[i]}
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.divider()


# ==========================================================
# Main Page
# ==========================================================

def show_profile():

    st.markdown(
        """
        <div class="page-title">
        👤 Financial Profile
        </div>

        <div class="page-subtitle">
        Complete your financial profile to receive
        personalized AI recommendations.
        </div>
        """,
        unsafe_allow_html=True,
    )

    show_progress(st.session_state.wizard_step)

    # ======================================================
    # STEP 1
    # ======================================================

    if st.session_state.wizard_step == 1:

        st.markdown(
            "<div class='card'>",
            unsafe_allow_html=True,
        )

        st.subheader("👤 Personal Information")

        st.write("")

        col1, col2 = st.columns(2)

        with col1:

            age = st.number_input(
                "Age",
                min_value=18,
                max_value=100,
                value=st.session_state.profile_data.get(
                    "age",
                    25
                )
            )

            occupation = st.text_input(
                "Occupation",
                value=st.session_state.profile_data.get(
                    "occupation",
                    ""
                )
            )

            family_size = st.number_input(
                "Family Size",
                min_value=1,
                max_value=20,
                value=st.session_state.profile_data.get(
                    "family_size",
                    1
                )
            )

        with col2:

            marital_status = st.selectbox(
                "Marital Status",
                [
                    "SINGLE",
                    "MARRIED",
                    "OTHER"
                ],
                index=[
                    "SINGLE",
                    "MARRIED",
                    "OTHER"
                ].index(
                    st.session_state.profile_data.get(
                        "marital_status",
                        "SINGLE"
                    )
                )
            )

            dependents = st.number_input(
                "Dependents",
                min_value=0,
                max_value=20,
                value=st.session_state.profile_data.get(
                    "dependents",
                    0
                )
            )

        st.write("")

        c1, c2 = st.columns([1,1])

        with c2:

            if st.button(
                "Next ➜",
                use_container_width=True
            ):

                if occupation.strip() == "":

                    st.error(
                        "Occupation is required."
                    )

                else:

                    st.session_state.profile_data.update({

                        "age": age,

                        "occupation": occupation,

                        "family_size": family_size,

                        "dependents": dependents,

                        "marital_status": marital_status,

                    })

                    st.session_state.wizard_step = 2

                    st.rerun()

        st.markdown(
            "</div>",
            unsafe_allow_html=True,
        )

        return

    # ======================================================
    # STEP 2 (Placeholder)
    # ======================================================

        # ======================================================
    # STEP 2 - INCOME DETAILS
    # ======================================================

    if st.session_state.wizard_step == 2:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("💰 Income Details")

        st.write("")

        col1, col2 = st.columns(2)

        with col1:

            monthly_income = st.number_input(
                "Monthly Income (₹)",
                min_value=0.0,
                value=float(
                    st.session_state.profile_data.get(
                        "monthly_income",
                        0
                    )
                ),
                step=1000.0
            )

            annual_income = st.number_input(
                "Annual Income (₹)",
                min_value=0.0,
                value=float(
                    st.session_state.profile_data.get(
                        "annual_income",
                        0
                    )
                ),
                step=10000.0
            )

        with col2:

            monthly_expenses = st.number_input(
                "Monthly Expenses (₹)",
                min_value=0.0,
                value=float(
                    st.session_state.profile_data.get(
                        "monthly_expenses",
                        0
                    )
                ),
                step=1000.0
            )

        st.write("")

        left, right = st.columns(2)

        with left:

            if st.button("⬅ Previous", use_container_width=True):

                st.session_state.wizard_step = 1
                st.rerun()

        with right:

            if st.button("Next ➜", use_container_width=True):

                if monthly_income <= 0:

                    st.error("Monthly income is required.")

                else:

                    st.session_state.profile_data.update({

                        "monthly_income": monthly_income,

                        "annual_income": annual_income,

                        "monthly_expenses": monthly_expenses,

                    })

                    st.session_state.wizard_step = 3

                    st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

        return


    # ======================================================
    # STEP 3 - ASSETS
    # ======================================================

    if st.session_state.wizard_step == 3:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("🏦 Assets & Liabilities")

        st.write("")

        col1, col2 = st.columns(2)

        with col1:

            existing_savings = st.number_input(

                "Existing Savings (₹)",

                min_value=0.0,

                value=float(
                    st.session_state.profile_data.get(
                        "existing_savings",
                        0
                    )
                ),

                step=1000.0

            )

            existing_investments = st.number_input(

                "Existing Investments (₹)",

                min_value=0.0,

                value=float(
                    st.session_state.profile_data.get(
                        "existing_investments",
                        0
                    )
                ),

                step=1000.0

            )

        with col2:

            existing_insurance = st.number_input(

                "Insurance Cover (₹)",

                min_value=0.0,

                value=float(
                    st.session_state.profile_data.get(
                        "existing_insurance",
                        0
                    )
                ),

                step=1000.0

            )

            debt_amount = st.number_input(

                "Total Debt (₹)",

                min_value=0.0,

                value=float(
                    st.session_state.profile_data.get(
                        "debt_amount",
                        0
                    )
                ),

                step=1000.0

            )

        st.write("")

        left, right = st.columns(2)

        with left:

            if st.button("⬅ Previous", key="back3", use_container_width=True):

                st.session_state.wizard_step = 2

                st.rerun()

        with right:

            if st.button("Next ➜", key="next3", use_container_width=True):

                st.session_state.profile_data.update({

                    "existing_savings": existing_savings,

                    "existing_investments": existing_investments,

                    "existing_insurance": existing_insurance,

                    "debt_amount": debt_amount,

                })

                st.session_state.wizard_step = 4

                st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

        return


    # ======================================================
    # STEP 4 PLACEHOLDER
    # ======================================================

        # ======================================================
    # STEP 4 - GOALS & RISK PROFILE
    # ======================================================

    if st.session_state.wizard_step == 4:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.subheader("🎯 Goals & Risk Profile")

        st.write("")

        risk_appetite = st.selectbox(
            "Risk Appetite",
            [
                "LOW",
                "MODERATE",
                "HIGH"
            ],
            index=[
                "LOW",
                "MODERATE",
                "HIGH"
            ].index(
                st.session_state.profile_data.get(
                    "risk_appetite",
                    "MODERATE"
                )
            )
        )

        financial_goals = st.text_area(
            "Financial Goals",
            value=st.session_state.profile_data.get(
                "financial_goals",
                ""
            ),
            placeholder="Example: Buy a house in 5 years, build an emergency fund, retire early..."
        )

        st.write("")

        left, right = st.columns(2)

        with left:

            if st.button(
                "⬅ Previous",
                key="back4",
                use_container_width=True
            ):
                st.session_state.wizard_step = 3
                st.rerun()

        with right:

            if st.button(
                "✅ Finish",
                key="finish",
                use_container_width=True
            ):

                if financial_goals.strip() == "":

                    st.error("Please enter your financial goals.")

                else:

                    st.session_state.profile_data.update({

                        "risk_appetite": risk_appetite,

                        "financial_goals": financial_goals

                    })

                    with st.spinner(
                        "Saving your financial profile..."
                    ):

                        response = ProfileService.create_profile(

                            profile_data=st.session_state.profile_data,

                            token=st.session_state.access_token

                        )

                    if response.status_code in [200, 201]:

                        st.success(
                            "🎉 Financial Profile Created Successfully!"
                        )

                        st.balloons()

                        st.session_state.profile_completed = True

                        st.session_state.wizard_step = 1

                        st.session_state.page = "Dashboard"

                        st.rerun()

                    else:

                        try:

                            detail = response.json().get(
                                "detail",
                                "Unable to create profile."
                            )

                        except Exception:

                            detail = "Unable to create profile."

                        st.error(detail)

        st.markdown("</div>", unsafe_allow_html=True)

        return
