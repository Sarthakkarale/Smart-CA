"""
=========================================================
Smart CA
Session State Manager
=========================================================

Centralized Streamlit session state.

Used Across:
- Login
- Register
- Dashboard
- Profile
- Reports
- Tax
- Settings
"""

import streamlit as st


def init_session():
    """
    Initialize application session variables.
    """

    defaults = {

        # -----------------------------
        # Navigation
        # -----------------------------
        "current_page": "login",

        # -----------------------------
        # Authentication
        # -----------------------------
        "is_authenticated": False,

        "access_token": None,

        "refresh_token": None,

        "current_user": None,

        # -----------------------------
        # Profile
        # -----------------------------
        "profile_completed": False,

        "profile_data": {},

        # -----------------------------
        # Dashboard
        # -----------------------------
        "dashboard_loaded": False,

        # -----------------------------
        # Wizard
        # -----------------------------
        "wizard_step": 1,

        # -----------------------------
        # UI
        # -----------------------------
        "sidebar_expanded": True,

        "theme": "light",

        "loading": False,

        "notification": None,

        # -----------------------------
        # Search
        # -----------------------------
        "search": "",

        # -----------------------------
        # Reports
        # -----------------------------
        "selected_report": None,

        # -----------------------------
        # Tax
        # -----------------------------
        "selected_financial_year": "2025-26",

        # -----------------------------
        # Investments
        # -----------------------------
        "selected_investment": None,

    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value


# =====================================================
# Navigation
# =====================================================

def set_page(page: str):
    """
    Change current page.
    """

    st.session_state.current_page = page


def get_page():

    return st.session_state.current_page


# =====================================================
# Authentication
# =====================================================

def login(
    access_token: str,
    refresh_token: str,
    user: dict,
):

    st.session_state.is_authenticated = True

    st.session_state.access_token = access_token

    st.session_state.refresh_token = refresh_token

    st.session_state.current_user = user


def logout():

    st.session_state.is_authenticated = False

    st.session_state.access_token = None

    st.session_state.refresh_token = None

    st.session_state.current_user = None

    st.session_state.current_page = "login"


# =====================================================
# Wizard
# =====================================================

def next_step():

    st.session_state.wizard_step += 1


def previous_step():

    if st.session_state.wizard_step > 1:

        st.session_state.wizard_step -= 1


def reset_wizard():

    st.session_state.wizard_step = 1


# =====================================================
# Loading
# =====================================================

def start_loading():

    st.session_state.loading = True


def stop_loading():

    st.session_state.loading = False


# =====================================================
# Notifications
# =====================================================

def show_notification(message: str):

    st.session_state.notification = message


def clear_notification():

    st.session_state.notification = None