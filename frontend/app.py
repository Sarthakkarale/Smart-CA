import streamlit as st
from streamlit_option_menu import option_menu
from pages.profile import profile_page
from pages.dashboard import dashboard_page
from pages.login import login_page 
from pages.register import register_page 

# 1. Page Config MUST be the very first Streamlit command
st.set_page_config(
    page_title="Smart CA",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Global CSS (Applies to all pages)
st.markdown("""
    <style>
    /* Hide native Streamlit sidebar nav */
    [data-testid="stSidebarNav"] {display: none;}
    
    /* Dark Sidebar - Using a very sleek dark slate color */
    [data-testid="stSidebar"] > div:first-child {
        background-color: #0F172A;
    }
    
    /* Light background for main app */
    .stApp { background-color: #F8F9FA; }
    
    /* Global Container Styling (White cards with shadow) */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #FFFFFF;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        border: none;
    }
    
    /* Remove default padding at the top of the sidebar */
    .css-1544g2n {padding-top: 1rem;}
    </style>
""", unsafe_allow_html=True)

# 3. Initialize Session State Variables
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "profile_completed" not in st.session_state:
    st.session_state.profile_completed = False

if "main_menu" not in st.session_state:
    st.session_state.main_menu = "Dashboard"

if "auth_page" not in st.session_state:
    st.session_state.auth_page = "login" 

# ==========================================================
# AUTH GUARD & PRE-LOGIN ROUTING
# ==========================================================
if not st.session_state.logged_in:
    if st.session_state.auth_page == "login":
        login_page()
    else:
        register_page()
        
    st.stop() # Halts execution here so the sidebar/app doesn't load

# ==========================================================
# THE MAIN APPLICATION (Only runs if logged_in == True)
# ==========================================================

# Create the persistent sidebar
with st.sidebar:
    # Logo and Title
    st.markdown("""
    <div style="display: flex; align-items: center; padding: 10px 0 30px 15px;">
        <span style="font-size: 26px; margin-right: 12px; color: #6366F1;">💠</span>
        <span style="color: white; font-size: 22px; font-weight: 700; letter-spacing: 0.5px;">Smart CA</span>
    </div>
    """, unsafe_allow_html=True)

    # The custom option menu
    selected = option_menu(
        menu_title=None,
        options=["Dashboard", "Financial Profile", "Documents", "AI Advisor", "Reports", "Goals", "Settings"],
        icons=["grid-fill", "person-badge-fill", "file-earmark-text-fill", "robot", "bar-chart-fill", "bullseye", "gear-fill"],
        default_index=0,
        key="main_menu",
        styles={
            "container": {
                "padding": "0!important", 
                "background-color": "#0F172A", 
                "border": "none",
                "border-radius": "0"
            },
            "icon": {
                "color": "#94A3B8", 
                "font-size": "18px"
            },
            "nav-link": {
                "font-size": "15px", 
                "text-align": "left", 
                "margin": "4px 12px", 
                "padding": "12px 15px",
                "color": "#94A3B8", 
                "border-radius": "8px", 
                "--hover-color": "#1E293B",
                "font-weight": "500"
            },
            "nav-link-selected": {
                "background-color": "#4F46E5", 
                "color": "white", 
                "font-weight": "600"
            },
        }
    )

    st.write("")
    st.write("")
    st.write("")
    
    # Styled Logout logic
    def do_logout():
        st.session_state.logged_in = False
        st.session_state.profile_completed = False
        st.session_state.auth_page = "login"

    st.markdown("""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <style>
    .logout-btn-container { margin: 0 12px; }
    .logout-btn-container button {
        background-color: transparent !important;
        color: #94A3B8 !important;
        border: none !important;
        padding: 12px 15px !important;
        border-radius: 8px !important;
        width: 100% !important;
        justify-content: flex-start !important;
        font-weight: 500 !important;
    }
    .logout-btn-container button:hover {
        background-color: #1E293B !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="logout-btn-container">', unsafe_allow_html=True)
        st.button("🚪 Logout", use_container_width=True, on_click=do_logout)
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================================
# ONBOARDING GUARD & ROUTING
# ==========================================================
if not st.session_state.profile_completed:
    profile_page()
else:
    if selected == "Dashboard":
        dashboard_page()
    elif selected == "Financial Profile":
        profile_page()
    else:
        st.info(f"The {selected} page is under construction.")
        