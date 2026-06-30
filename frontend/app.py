import streamlit as st

# ==========================
# Components
# ==========================
from components.styles import load_styles
from components.sidebar import show_sidebar
from components.navbar import show_navbar

# ==========================
# Pages
# ==========================
from pages.login import show_login
from pages.register import show_register
from pages.dashboard import show_dashboard
from pages.profile import show_profile
from pages.documents import show_documents
from pages.advisor import show_advisor
from pages.reports import show_reports
from pages.settings import show_settings

# ==========================
# Session
# ==========================
from utils.session import initialize_session

# ==========================
# Streamlit Config
# ==========================
st.set_page_config(
    page_title="Smart CA",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================
# Load Theme
# ==========================
load_styles()

# ==========================
# Initialize Session
# ==========================
initialize_session()

# ==========================
# Default Session Values
# ==========================
if "page" not in st.session_state:
    st.session_state.page = "Login"

# ==========================
# Authentication
# ==========================
if not st.session_state.logged_in:

    if st.session_state.page == "Register":
        show_register()

    else:
        show_login()

    st.stop()

# ==========================
# Sidebar
# ==========================
selected_page = show_sidebar()

if selected_page:
    st.session_state.page = selected_page

# ==========================
# Navbar
# ==========================
user_name = "User"

if st.session_state.current_user:
    user_name = st.session_state.current_user.get(
        "full_name",
        "User"
    )

show_navbar(
    st.session_state.page,
    user_name
)

# ==========================
# Routing
# ==========================
page = st.session_state.page

if page == "Dashboard":
    show_dashboard()

elif page == "Financial Profile":
    show_profile()

elif page == "Documents":
    show_documents()

elif page == "AI Advisor":
    show_advisor()

elif page == "Reports":
    show_reports()

elif page == "Settings":
    show_settings()

elif page == "Logout":
    st.session_state.logged_in = False
    st.session_state.current_user = None
    st.session_state.access_token = None
    st.session_state.refresh_token = None
    st.session_state.page = "Login"
    st.rerun()

else:
    show_dashboard()