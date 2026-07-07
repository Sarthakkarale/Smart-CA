import streamlit as st
import time
from services.auth_service import AuthService

def register_page():
    st.markdown("""
        <style>
        [data-testid="collapsedControl"] { display: none; }
        .stApp { background-color: #F8F9FA; }
        [data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #FFFFFF;
            border-radius: 16px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.025);
            border: 1px solid #F3F4F6;
            padding: 10px;
        }
        .stButton > button[kind="primary"] {
            background-color: #4F46E5;
            color: white;
            border-radius: 8px;
            font-weight: 600;
            padding: 0.5rem 1rem;
            border: none;
            transition: all 0.2s ease;
        }
        .stButton > button[kind="primary"]:hover {
            background-color: #4338CA;
            box-shadow: 0 4px 6px -1px rgba(79, 70, 229, 0.4);
        }
        </style>
    """, unsafe_allow_html=True)

    st.write("<br><br><br>", unsafe_allow_html=True)

    left_col, right_col = st.columns([1.1, 1], gap="large")

    with left_col:
        st.markdown("""
        <div style="padding: 20px 20px 20px 40px;">
            <div style="display: flex; align-items: center; margin-bottom: 30px;">
                <span style="font-size: 36px; margin-right: 12px; color: #4F46E5;">💠</span>
                <span style="color: #0F172A; font-size: 32px; font-weight: 800; letter-spacing: -0.5px;">Smart CA</span>
            </div>
            <h1 style="color: #111827; font-size: 42px; font-weight: 800; margin-bottom: 15px; line-height: 1.2;">Join Smart CA Today</h1>
            <p style="color: #4B5563; font-size: 17px; line-height: 1.6; margin-bottom: 40px; max-width: 90%;">Create your account to unlock AI-powered financial insights, personalized tax planning, and seamless document analysis.<br><br>Take control of your financial future in minutes.</p>
            <div style="display: flex; align-items: center; gap: 15px; background-color: #EEF2FF; padding: 15px 20px; border-radius: 12px; width: fit-content;">
                <span style="font-size: 30px;">🚀</span>
                <span style="color: #4338CA; font-weight: 600; font-size: 15px;">Fast, secure, and intelligent.</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with right_col:
        with st.container(border=True):
            st.markdown("<h3 style='color: #111827; margin-bottom: 5px; font-size: 24px; font-weight: 700;'>Create Account</h3><p style='color: #6B7280; font-size: 15px; margin-bottom: 25px;'>Please fill in your details to get started.</p>", unsafe_allow_html=True)
            
            full_name = st.text_input("Full Name", placeholder="e.g. Sarthak Karale")
            email = st.text_input("Email Address", placeholder="Enter your email")
            
            col1, col2 = st.columns(2)
            with col1: password = st.text_input("Password", type="password", placeholder="Create password")
            with col2: confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm password")
            
            st.write("")
            error_placeholder = st.empty()
            
            if st.button("Sign Up", type="primary", use_container_width=True):
                if not full_name or not email or not password or not confirm_password:
                    error_placeholder.error("Please fill in all fields.")
                elif password != confirm_password:
                    error_placeholder.error("Passwords do not match.")
                else:
                    with st.spinner("Creating account..."):
                        # --- REAL BACKEND CALL ---
                        response = AuthService.register(full_name, email, password)
                        
                        if response is None:
                            error_placeholder.error("🚨 Backend server is unreachable. Is FastAPI running?")
                        elif response.status_code in [200, 201]:
                            st.success("Account created successfully! Redirecting to login...")
                            time.sleep(1)
                            st.session_state.auth_page = "login"
                            st.rerun()
                        else:
                            try:
                                error_placeholder.error(response.json().get("detail", "Failed to create account. Email may already exist."))
                            except:
                                error_placeholder.error("Failed to create account.")
            
            st.write("")
            st.markdown("<div style='text-align: center; margin-top: 10px;'><span style='color: #6B7280; font-size: 14px;'>Already have an account?</span></div>", unsafe_allow_html=True)
            def go_to_login(): st.session_state.auth_page = "login"
            st.button("Sign In Instead", use_container_width=True, on_click=go_to_login)