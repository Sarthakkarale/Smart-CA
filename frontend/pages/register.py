import streamlit as st

from services.auth_service import AuthService


def show_register():

    left, right = st.columns([1.2, 1])

    # =====================================================
    # LEFT SIDE
    # =====================================================

    with left:

        st.markdown("""
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
                Create Your Account
            </h3>

            <p style="
                color:#64748B;
                font-size:18px;
                line-height:1.8;
            ">

            Join Smart CA and start managing your
            finances with AI powered insights.

            </p>

        </div>
        """, unsafe_allow_html=True)

    # =====================================================
    # RIGHT SIDE
    # =====================================================

    with right:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        st.markdown(
            "<h2 style='text-align:center;'>Create Account</h2>",
            unsafe_allow_html=True,
        )

        st.write("")

        full_name = st.text_input(
            "Full Name",
            placeholder="Enter full name"
        )

        email = st.text_input(
            "Email",
            placeholder="Enter email"
        )

        phone = st.text_input(
            "Phone",
            placeholder="9876543210"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password"
        )

        role = st.selectbox(
            "Role",
            [
                "User"
            ]
        )

        st.write("")

        if st.button(
            "Create Account",
            use_container_width=True,
            type="primary"
        ):

            if (
                full_name == ""
                or email == ""
                or password == ""
            ):

                st.error("Please fill all required fields.")

            elif password != confirm_password:

                st.error("Passwords do not match.")

            else:

                payload = {

                    "full_name": full_name,

                    "email": email,

                    "phone": phone,

                    "password": password,

                    "role_id": 2

                }

                with st.spinner(
                    "Creating account..."
                ):

                    response = AuthService.register(
                        payload
                    )

                if response.status_code in [200, 201]:

                    st.success(
                        "Account created successfully."
                    )

                    st.balloons()

                    st.session_state.page = "Login"

                    st.rerun()

                else:

                    try:

                        detail = response.json().get(
                            "detail",
                            "Registration failed."
                        )

                    except:

                        detail = "Registration failed."

                    st.error(detail)

        st.write("")

        c1, c2, c3 = st.columns([1,2,1])

        with c2:

            if st.button(
                "Back to Login",
                use_container_width=True
            ):

                st.session_state.page = "Login"

                st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)