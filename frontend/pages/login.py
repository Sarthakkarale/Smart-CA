import streamlit as st

from services.auth_service import AuthService
from utils.session import login_user


def show_login():

    left, right = st.columns([1.2, 1])

    # ==========================================
    # Left Side
    # ==========================================
    with left:

        st.markdown(
            """
            <div style="padding:80px 40px;">

                <h1 style="
                    font-size:48px;
                    color:#1E293B;
                    margin-bottom:10px;
                ">
                    💼 Smart CA
                </h1>

                <h3 style="
                    color:#6D5EF8;
                    margin-bottom:20px;
                ">
                    AI Powered Financial Assistant
                </h3>

                <p style="
                    color:#64748B;
                    font-size:18px;
                    line-height:1.8;
                ">

                Manage your finances, upload documents,
                receive AI powered recommendations and
                track your financial health — all in one place.

                </p>

            </div>
            """,
            unsafe_allow_html=True,
        )

    # ==========================================
    # Right Side
    # ==========================================
    with right:

        st.markdown(
            """
            <div class="card">
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <h2 style="text-align:center;">
                Welcome Back 👋
            </h2>
            """,
            unsafe_allow_html=True,
        )

        st.write("")

        email = st.text_input(
            "Email",
            placeholder="Enter your email"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password"
        )

        st.write("")

        if st.button(
            "Login",
            use_container_width=True,
            type="primary"
        ):

            if not email or not password:

                st.error(
                    "Please enter email and password."
                )

            else:

                with st.spinner(
                    "Signing in..."
                ):

                    response = AuthService.login(
                        email,
                        password
                    )

                if response.status_code == 200:

                    data = response.json()

                    access_token = data["access_token"]

                    refresh_token = data["refresh_token"]

                    me = AuthService.get_me(
                        access_token
                    )

                    if me.status_code == 200:

                        user = me.json()

                        login_user(
                            user=user,
                            access_token=access_token,
                            refresh_token=refresh_token
                        )

                        st.session_state.page = "Dashboard"

                        st.success(
                            "Login Successful!"
                        )

                        st.rerun()

                    else:

                        st.error(
                            "Unable to fetch user profile."
                        )

                else:

                    try:

                        detail = response.json().get(
                            "detail",
                            "Invalid credentials."
                        )

                    except Exception:

                        detail = "Login failed."

                    st.error(detail)

        st.write("")

        c1, c2, c3 = st.columns([1, 2, 1])

        with c2:

            if st.button(
                "Create Account",
                use_container_width=True
            ):

                st.session_state.page = "Register"

                st.rerun()

        st.markdown(
            "</div>",
            unsafe_allow_html=True,
        )