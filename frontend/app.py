import streamlit as st

# ==========================================
# Global Styles
# ==========================================

from assets.styles import load_css

# ==========================================
# State
# ==========================================

from state.auth_state import AuthState

# ==========================================
# Pages
# ==========================================

from pages.login import login_page
from pages.register import register_page
from pages.profile import profile_page
from pages.dashboard import dashboard_page

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Smart CA",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ==========================================
# Load CSS
# ==========================================

load_css()

# ==========================================
# Hide Streamlit UI
# ==========================================

st.markdown(
    """
    <style>

    #MainMenu{
        visibility:hidden;
    }

    header{
        visibility:hidden;
    }

    footer{
        visibility:hidden;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# Session Defaults
# ==========================================

DEFAULT_STATE = {

    "page": "login",

    "logged_in": False,

    "access_token": None,

    "refresh_token": None,

    "user": None,

    "profile_completed": False,

}

for key, value in DEFAULT_STATE.items():

    if key not in st.session_state:

        st.session_state[key] = value

# ==========================================
# Authentication Guard
# ==========================================

public_pages = {

    "login",
    "register",

}

if (

    not AuthState.is_logged_in()

    and st.session_state.page not in public_pages

):

    st.session_state.page = "login"

# ==========================================
# Routing
# ==========================================

PAGE_ROUTES = {

    "login": login_page,

    "register": register_page,

    "profile": profile_page,

    "dashboard": dashboard_page,

}

page = st.session_state.page

if page in PAGE_ROUTES:

    PAGE_ROUTES[page]()

else:

    st.session_state.page = "login"

    st.rerun()