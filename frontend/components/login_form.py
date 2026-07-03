import streamlit as st

from services.auth_service import AuthService
from state.auth_state import AuthState

from utils.validators import (
    validate_email,
    validate_password,
)


def login_form():
    """
    Smart CA Login Form
    """

    # =====================================================
    # Header
    # =====================================================

    st.header("Login")
    st.caption("Please sign in to continue")

    st.write("")

    # =====================================================
    # Login Form
    # =====================================================

    with st.form("login_form", clear_on_submit=False):

        email = st.text_input(
            "Email Address",
            placeholder="Enter your email",
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password",
        )

        left, right = st.columns([1, 1])

        with left:
            remember = st.checkbox("Remember me")

        with right:
            st.write("")
            st.caption("Forgot Password?")

        st.write("")

        login_clicked = st.form_submit_button(
            "Login",
            type="primary",
            use_container_width=True,
        )

    # =====================================================
    # Register Link
    # =====================================================

    st.write("")
    st.divider()
    st.write("")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.caption("Don't have an account?")

    with col2:

        if st.button(
            "Create Account",
            key="register_button",
            type="secondary",
        ):
            st.session_state.page = "register"
            st.rerun()

    # =====================================================
    # Login API
    # =====================================================

    if login_clicked:

        valid, message = validate_email(email)

        if not valid:
            st.error(message)
            return

        valid, message = validate_password(password)

        if not valid:
            st.error(message)
            return

        with st.spinner("Signing in..."):

            response = AuthService.login(
                email=email,
                password=password,
            )

        if response.get("success"):

            AuthState.login(
                access_token=response["access_token"],
                refresh_token=response["refresh_token"],
                user=response["user"],
            )

            st.success(response["message"])

            # Profile check will be added later
            st.session_state.page = "dashboard"

            st.rerun()

        else:

            st.error(
                response.get(
                    "message",
                    "Login failed.",
                )
            )