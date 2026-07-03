import streamlit as st

from services.auth_service import AuthService

from utils.validators import (
    validate_email,
    validate_name,
    validate_password,
    validate_phone,
)


def register_form():
    """
    Smart CA Register Form
    """

    # =====================================================
    # Header
    # =====================================================

    st.header("Create Account")
    st.caption("Create your Smart CA account")

    st.write("")

    # =====================================================
    # Register Form
    # =====================================================

    with st.form("register_form", clear_on_submit=False):

        full_name = st.text_input(
            "Full Name",
            placeholder="Enter your full name",
        )

        email = st.text_input(
            "Email Address",
            placeholder="Enter your email",
        )

        phone = st.text_input(
            "Phone Number",
            placeholder="Enter your phone number",
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Create your password",
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password",
            placeholder="Confirm your password",
        )

        st.write("")

        register_clicked = st.form_submit_button(
            "Create Account",
            type="primary",
            use_container_width=True,
        )

    # =====================================================
    # Login Link
    # =====================================================

    st.write("")
    st.divider()
    st.write("")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.caption("Already have an account?")

    with col2:

        if st.button(
            "Login",
            key="login_button",
            type="secondary",
        ):
            st.session_state.page = "login"
            st.rerun()

    # =====================================================
    # Register API
    # =====================================================

    if register_clicked:

        valid, message = validate_name(full_name)

        if not valid:
            st.error(message)
            return

        valid, message = validate_email(email)

        if not valid:
            st.error(message)
            return

        valid, message = validate_phone(phone)

        if not valid:
            st.error(message)
            return

        valid, message = validate_password(password)

        if not valid:
            st.error(message)
            return

        if password != confirm_password:

            st.error("Passwords do not match.")
            return

        with st.spinner("Creating your account..."):

            response = AuthService.register(
                full_name=full_name,
                email=email,
                phone=phone,
                password=password,
            )

        if response.get("success"):

            st.success(response["message"])

            st.info("Please login with your new account.")

            st.session_state.page = "login"

            st.rerun()

        else:

            st.error(
                response.get(
                    "message",
                    "Registration failed.",
                )
            )