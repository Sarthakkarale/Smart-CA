"""
Authentication session state manager.
"""

import streamlit as st


class AuthState:

    @staticmethod
    def is_logged_in() -> bool:
        return st.session_state.get("logged_in", False)

    @staticmethod
    def login(
        access_token: str,
        refresh_token: str,
        user: dict,
    ):

        st.session_state.logged_in = True
        st.session_state.access_token = access_token
        st.session_state.refresh_token = refresh_token
        st.session_state.user = user

    @staticmethod
    def logout():

        st.session_state.logged_in = False
        st.session_state.access_token = None
        st.session_state.refresh_token = None
        st.session_state.user = None
        st.session_state.page = "login"

    @staticmethod
    def get_user():

        return st.session_state.get("user")

    @staticmethod
    def get_access_token():

        return st.session_state.get("access_token")

    @staticmethod
    def get_refresh_token():

        return st.session_state.get("refresh_token")