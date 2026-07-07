"""
=========================================================
Smart CA
Register Page
=========================================================
"""

import streamlit as st

from components.auth_layout import render_auth_layout
from utils.router import go_login


def _register_form():
    """
    Register form UI.
    """

    with st.form(
        "register_form",
        clear_on_submit=False,
    ):

        full_name = st.text_input(
            "Full Name",
            placeholder="Enter your full name",
            key="register_name",
        )

        email = st.text_input(
            "Email Address",
            placeholder="Enter your email address",
            key="register_email",
        )

        phone = st.text_input(
            "Phone Number",
            placeholder="Enter your mobile number",
            key="register_phone",
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Create a strong password",
            key="register_password",
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password",
            placeholder="Confirm your password",
            key="register_confirm_password",
        )

        agree = st.checkbox(
            "I agree to the Terms & Conditions and Privacy Policy",
            key="register_terms",
        )

        st.info(
            """
Password Requirements

• Minimum 8 characters

• One uppercase letter

• One lowercase letter

• One number

• One special character
            """
        )

        submitted = st.form_submit_button(
            "Create Account",
            use_container_width=True,
        )

    if submitted:

        if not full_name.strip():

            st.error("Please enter your full name.")

            return

        if not email.strip():

            st.error("Please enter your email.")

            return

        if not phone.strip():

            st.error("Please enter your phone number.")

            return

        if not password:

            st.error("Please create a password.")

            return

        if password != confirm_password:

            st.error("Passwords do not match.")

            return

        if not agree:

            st.warning(
                "Please accept the Terms & Conditions."
            )

            return

        # Sprint 1
        # UI Only

        st.success(
            "Account created successfully! (UI Demo)"
        )

    st.divider()

    st.caption(
        "Already have an account?"
    )

    if st.button(
        "Sign In",
        use_container_width=True,
        key="login_button",
    ):

        go_login()
def render_page():
    """
    Render Register Page.
    """

    render_auth_layout(
        title="Create Your Account 🚀",
        subtitle=(
            "Start your financial journey with Smart CA.\n"
            "Create an account to access AI-powered financial assistance."
        ),
        form_renderer=_register_form,
    )

    st.markdown("<br>")

    left, center, right = st.columns([1, 2, 1])

    with center:

        st.caption(
            "Secure • Fast • AI Powered • Trusted by Middle Class Families"
        )

        st.markdown(
            """
            <div style="
                text-align:center;
                color:#94A3B8;
                font-size:13px;
                padding-top:10px;
            ">
                Smart CA © 2026
            </div>
            """,
            unsafe_allow_html=True,
        )