import streamlit as st
import time
from services.auth_service import AuthService
from services.profile_service import ProfileService

def login_page():
    # --- CSS Styles ---
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
            <h1 style="color: #111827; font-size: 42px; font-weight: 800; margin-bottom: 15px; line-height: 1.2;">Welcome Back!</h1>
            <p style="color: #4B5563; font-size: 17px; line-height: 1.6; margin-bottom: 40px; max-width: 90%;">Login to continue to your Smart CA account.<br><br>Manage your taxes, investments, financial planning, OCR document analysis, AI insights and reports from one intelligent platform.</p>
            <div style="display: flex; align-items: center; gap: 15px; background-color: #EEF2FF; padding: 15px 20px; border-radius: 12px; width: fit-content;">
                <span style="font-size: 30px;">🛡️</span>
                <span style="color: #4338CA; font-weight: 600; font-size: 15px;">Bank-level security & encryption.</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with right_col:
        with st.container(border=True):
            st.markdown("<h3 style='color: #111827; margin-bottom: 5px; font-size: 24px; font-weight: 700;'>Login</h3><p style='color: #6B7280; font-size: 15px; margin-bottom: 25px;'>Please sign in to continue</p>", unsafe_allow_html=True)
            
            email = st.text_input("Email Address", placeholder="Enter your email")
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            
            c1, c2 = st.columns(2)
            with c1: st.checkbox("Remember me")
            with c2: st.markdown("<p style='text-align: right; margin-top: 10px;'><a href='#' style='color: #4F46E5; text-decoration: none; font-size: 14px; font-weight: 500;'>Forgot Password?</a></p>", unsafe_allow_html=True)
            
            st.write("")
            error_placeholder = st.empty()
            
            if st.button("Login", type="primary", use_container_width=True):
                if email and password:
                    with st.spinner("Authenticating..."):
                        # --- REAL BACKEND CALL ---
                        response = AuthService.login(email, password)
                        
                        if response is None:
                            error_placeholder.error("🚨 Backend server is unreachable. Is FastAPI running?")
                        elif response.status_code == 200:
                            data = response.json()
                            
                            st.session_state.access_token = data.get("access_token")
                            
                            # Check if profile exists
                            profile_res = ProfileService.get_profile()
                            if profile_res and profile_res.status_code == 200:
                                st.session_state.profile_completed = True
                                st.session_state.profile = profile_res.json() # Load their data for the dashboard
                                user_data = profile_res.json().get("personal_info", {})
                                st.session_state.user = {"full_name": user_data.get("full_name", "User"), "email": email}
                            else:
                                st.session_state.profile_completed = False
                                st.session_state.user = {"full_name": email.split('@')[0], "email": email} # Fallback
                                
                            st.session_state.logged_in = True
                            st.rerun()
                        else:
                            try:
                                error_placeholder.error(response.json().get("detail", "Invalid credentials."))
                            except:
                                error_placeholder.error("Invalid credentials.")
                else:
                    error_placeholder.error("Please enter both email and password.")
                    
            st.write("")
            st.markdown("<div style='text-align: center; margin-top: 10px;'><span style='color: #6B7280; font-size: 14px;'>Don't have an account?</span></div>", unsafe_allow_html=True)
            def go_to_register(): st.session_state.auth_page = "register"
            st.button("Create Account", use_container_width=True, on_click=go_to_register)