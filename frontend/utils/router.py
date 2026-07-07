"""
=========================================================
Smart CA
Router Utility
=========================================================

Centralized navigation helper for the Streamlit frontend.

All page navigation should go through this module.

Example:
--------
from utils.router import navigate

if st.button("Dashboard"):
    navigate("dashboard")
"""

import streamlit as st


# ==========================================================
# Core Navigation
# ==========================================================

def navigate(page: str) -> None:
    """
    Navigate to another page.
    """

    st.session_state.current_page = page
    st.rerun()


def get_current_page() -> str:
    """
    Return current active page.
    """

    return st.session_state.get("current_page", "login")


# ==========================================================
# Authentication
# ==========================================================

def go_login():
    navigate("login")


def go_register():
    navigate("register")


def go_logout():
    navigate("logout")


# ==========================================================
# Dashboard
# ==========================================================

def go_dashboard():
    navigate("dashboard")


# ==========================================================
# Profile
# ==========================================================

def go_profile():
    navigate("profile")


def go_create_profile():
    navigate("create_profile")


def go_edit_profile():
    navigate("edit_profile")


# ==========================================================
# Reports
# ==========================================================

def go_reports():
    navigate("reports")


# ==========================================================
# Investments
# ==========================================================

def go_investments():
    navigate("investments")


# ==========================================================
# Tax
# ==========================================================

def go_tax():
    navigate("tax")


# ==========================================================
# Settings
# ==========================================================

def go_settings():
    navigate("settings")


# ==========================================================
# Future Modules
# ==========================================================

def go_documents():
    navigate("documents")


def go_ai_advisor():
    navigate("advisor")


# ==========================================================
# Utility
# ==========================================================

def is_page(page: str) -> bool:
    """
    Check if the supplied page is active.

    Example:
        if is_page("dashboard"):
            ...
    """

    return get_current_page() == page