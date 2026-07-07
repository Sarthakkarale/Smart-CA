"""
=========================================================
Smart CA
Login Page
=========================================================
"""

import streamlit as st

from components.auth_layout import render_auth_layout
from utils.router import go_dashboard, go_register


def _login_form():
    """
    Login form UI.
    """

    with st.form(
        "login_form",
        clear_on_submit=False,
    ):

        st.text_input(
            "Email Address",
            placeholder="Enter your email",
            key="login_email",
        )

        st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password",
            key="login_password",
        )

        left, right = st.columns([1, 1])

        with left:

            st.checkbox(
                "Remember Me",
                key="remember_me",
            )

        with right:

            st.markdown(
                "<p style='text-align:right;color:#6D5EF8;font-size:14px;'>Forgot Password?</p>",
                unsafe_allow_html=True,
            )

        st.write("")

        submitted = st.form_submit_button(
            "Sign In",
            use_container_width=True,
        )

    if submitted:

        email = st.session_state.login_email.strip()

        password = st.session_state.login_password.strip()

        if email == "":

            st.error("Please enter your email.")

            return

        if password == "":

            st.error("Please enter your password.")

            return

        # Sprint 1
        # Backend integration in Sprint 2

        st.success("Login Successful")

        go_dashboard()

    st.divider()

    st.caption("Don't have an account?")

    if st.button(
        "Create New Account",
        use_container_width=True,
    ):

        go_register()

def render_page():
    """
    Render Login Page.
    """

    render_auth_layout(
        title="Welcome Back 👋",
        subtitle=(
            "Sign in to your Smart CA account to continue "
            "managing your finances."
        ),
        form_renderer=_login_form,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    left, center, right = st.columns([1, 2, 1])

    with center:

        st.caption(
            "Trusted by thousands of families for secure financial management."
        )

        st.markdown(
            """
            <div style="
                text-align:center;
                font-size:13px;
                color:#94A3B8;
                padding-top:12px;
            ">
                Version 1.0 • Smart CA
            </div>
            """,
            unsafe_allow_html=True,
        )