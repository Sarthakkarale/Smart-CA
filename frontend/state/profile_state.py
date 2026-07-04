import streamlit as st


DEFAULT_PROFILE = {
    "personal": {
        "full_name": "",
        "dob": None,
        "gender": "",
        "phone": "",
        "email": "",
        "city": "",
        "state": "",
        "pincode": "",
    },

    "tax": {
        "pan": "",
        "aadhaar": "",
        "tax_regime": "",
        "itr_type": "",
        "gst_number": "",
        "gst_registered": False,
    },

    "professional": {
        "employment_type": "",
        "occupation": "",
        "company_name": "",
        "annual_income": 0,
        "monthly_income": 0,
        "experience": 0,
    },

    "financial": {
        "bank_name": "",
        "monthly_expense": 0,
        "investments": 0,
        "loans": 0,
        "insurance": 0,
        "emergency_fund": 0,
    },

    "goals": {
        "retirement": False,
        "house": False,
        "car": False,
        "education": False,
        "vacation": False,
        "wealth_creation": False,
    }
}


def initialize_profile_state():

    if "profile" not in st.session_state:

        st.session_state.profile = DEFAULT_PROFILE.copy()

    if "profile_step" not in st.session_state:

        st.session_state.profile_step = 1