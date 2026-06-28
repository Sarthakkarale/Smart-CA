import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Smart CA Auth", page_icon="💼", layout="wide")

if "access_token" not in st.session_state:
    st.session_state.access_token = None
if "refresh_token" not in st.session_state:
    st.session_state.refresh_token = None
if "user" not in st.session_state:
    st.session_state.user = None
if "page" not in st.session_state:
    st.session_state.page = "Register"


def auth_headers():
    return {"Authorization": f"Bearer {st.session_state.access_token}"}


st.markdown("""
<style>
[data-testid="stHeader"] {
    display: none;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617 0%, #0f172a 100%);
    border-right: 1px solid rgba(148,163,184,0.25);
    width: 330px !important;
}

.stApp {
    background:
        radial-gradient(circle at top right, rgba(236,72,153,0.45), transparent 30%),
        radial-gradient(circle at center left, rgba(79,70,229,0.35), transparent 35%),
        linear-gradient(135deg, #020617 0%, #111827 45%, #2e1065 100%);
    color: white;
}

.block-container {
    padding-top: 2rem;
    max-width: 1180px;
}

.logo-row {
    display: flex;
    align-items: center;
    gap: 14px;
    margin: 24px 0 4px 0;
}

.logo-icon {
    width: 54px;
    height: 54px;
    border-radius: 18px;
    background: linear-gradient(135deg, #ec4899, #7c3aed, #2563eb);
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 28px;
    box-shadow: 0 15px 35px rgba(124,58,237,0.45);
}

.logo-title {
    font-size: 31px;
    font-weight: 900;
    color: #ffffff;
}

.logo-subtitle {
    color: #cbd5e1;
    font-size: 15px;
    margin-bottom: 60px;
}

.nav-btn {
    padding: 16px 18px;
    border-radius: 12px;
    margin: 8px 0;
    color: #e5e7eb;
    font-size: 17px;
    font-weight: 700;
}

.nav-active {
    background: linear-gradient(90deg, #ec4899, #8b5cf6, #4f46e5);
    box-shadow: 0 12px 30px rgba(124,58,237,0.4);
}

.trust-card {
    position: fixed;
    bottom: 28px;
    left: 24px;
    width: 275px;
    padding: 26px;
    border-radius: 18px;
    background: rgba(30,41,59,0.65);
    border: 1px solid rgba(148,163,184,0.25);
    text-align: center;
    box-shadow: 0 20px 60px rgba(0,0,0,0.35);
}

.trust-icon {
    width: 52px;
    height: 52px;
    margin: auto;
    border-radius: 50%;
    background: linear-gradient(135deg, #8b5cf6, #2563eb);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
}

.secure-badge {
    position: fixed;
    top: 30px;
    right: 34px;
    padding: 14px 22px;
    border-radius: 16px;
    background: rgba(15,23,42,0.65);
    border: 1px solid rgba(148,163,184,0.25);
    color: #ffffff;
    font-weight: 800;
    box-shadow: 0 18px 45px rgba(0,0,0,0.35);
}

.auth-card {
    background: rgba(15,23,42,0.72);
    border: 1px solid rgba(148,163,184,0.25);
    border-radius: 22px;
    padding: 34px 46px 36px 46px;
    box-shadow: 0 30px 90px rgba(0,0,0,0.45);
    backdrop-filter: blur(16px);
}

.form-icon {
    width: 76px;
    height: 76px;
    margin: auto;
    border-radius: 50%;
    background: linear-gradient(135deg, #ec4899, #8b5cf6, #4f46e5);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 38px;
    box-shadow: 0 15px 35px rgba(124,58,237,0.55);
}

.main-title {
    font-size: 34px;
    font-weight: 900;
    text-align: center;
    margin-top: 16px;
    color: #ffffff;
}

.main-subtitle {
    color: #cbd5e1;
    text-align: center;
    font-size: 16px;
    margin-bottom: 16px;
}

.title-line {
    width: 95px;
    height: 4px;
    border-radius: 10px;
    margin: 20px auto 28px auto;
    background: linear-gradient(90deg, #8b5cf6, #ec4899);
}

label {
    color: #f8fafc !important;
    font-weight: 800 !important;
}

.stTextInput input {
    background: rgba(15,23,42,0.8) !important;
    border: 1px solid rgba(148,163,184,0.28) !important;
    border-radius: 13px !important;
    color: white !important;
    height: 52px;
}

.stSelectbox div[data-baseweb="select"] > div {
    background: rgba(15,23,42,0.8) !important;
    border: 1px solid rgba(148,163,184,0.28) !important;
    border-radius: 13px !important;
    color: white !important;
    min-height: 52px;
}

.req-box {
    margin-top: 12px;
    margin-bottom: 24px;
    padding: 20px;
    border-radius: 15px;
    background: rgba(2,6,23,0.55);
    border: 1px solid rgba(148,163,184,0.25);
}

.req-title {
    color: #a855f7;
    font-weight: 900;
    margin-bottom: 16px;
}

.req-grid {
    display: flex;
    justify-content: space-between;
    gap: 12px;
    color: #d1d5db;
    font-size: 14px;
}

.success-box {
    background: rgba(6,78,59,0.9);
    color: #d1fae5;
    padding: 15px 18px;
    border-radius: 12px;
    font-weight: 800;
    margin-top: 16px;
}

.error-box {
    background: rgba(127,29,29,0.92);
    color: #fee2e2;
    padding: 15px 18px;
    border-radius: 12px;
    font-weight: 800;
    margin-top: 16px;
}

.info-box {
    background: rgba(30,64,175,0.55);
    color: #dbeafe;
    padding: 15px 18px;
    border-radius: 12px;
    font-weight: 700;
    margin-top: 16px;
}

div.stButton > button {
    width: 100%;
    height: 58px;
    border-radius: 14px;
    border: none;
    color: white;
    font-size: 18px;
    font-weight: 900;
    background: linear-gradient(90deg, #ec4899, #a855f7, #4f46e5);
    box-shadow: 0 18px 40px rgba(124,58,237,0.35);
}

div.stButton > button:hover {
    transform: translateY(-1px);
    border: none;
}

.bottom-link {
    text-align: center;
    color: #cbd5e1;
    margin-top: 20px;
    font-size: 16px;
}

.profile-card {
    background: rgba(2,6,23,0.45);
    border: 1px solid rgba(148,163,184,0.22);
    border-radius: 16px;
    padding: 20px;
    margin-top: 16px;
}
</style>
""", unsafe_allow_html=True)


# Sidebar
with st.sidebar:
    st.markdown("""
    <div class="logo-row">
        <div class="logo-icon">📈</div>
        <div>
            <div class="logo-title">Smart CA</div>
            <div class="logo-subtitle">AI Powered Financial Advisor</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    pages = [
        ("Register", "👥"),
        ("Login", "🔒"),
        ("My Profile", "👤"),
        ("Logout", "↪️"),
        ("Logout All Devices", "📱"),
        ("About", "ℹ️"),
    ]

    for name, icon in pages:
        active = "nav-active" if st.session_state.page == name else ""
        if st.button(f"{icon}  {name}", key=name):
            st.session_state.page = name
            st.rerun()

    st.markdown("""
    <div class="trust-card">
        <div class="trust-icon">🛡️</div>
        <h3>Secure & Trusted</h3>
        <p style="color:#cbd5e1;">Your data is protected with industry-leading security.</p>
    </div>
    """, unsafe_allow_html=True)


st.markdown('<div class="secure-badge">🛡️ Secure Connection 🟢</div>', unsafe_allow_html=True)

left, center, right = st.columns([0.2, 2.2, 0.2])

with center:
    

    page = st.session_state.page

    if page == "Register":
        st.markdown('<div class="form-icon">👥</div>', unsafe_allow_html=True)
        st.markdown('<div class="main-title">Create Your Account</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="main-subtitle">Join Smart CA and take control of your financial future</div>',
            unsafe_allow_html=True
        )
        st.markdown('<div class="title-line"></div>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            full_name = st.text_input("Full Name", placeholder="Enter your full name")
            phone = st.text_input("Phone Number", placeholder="Enter your 10 digit mobile number")

        with col2:
            email = st.text_input("Email Address", placeholder="Enter your email address")
            role = st.selectbox("Select Role", ["USER", "CA"])

        password = st.text_input("Password", type="password", placeholder="Create a strong password")

        st.markdown("""
        <div class="req-box">
            <div class="req-title">🛡️ Password Requirements</div>
            <div class="req-grid">
                <span>✅ At least 8 characters</span>
                <span>✅ One uppercase letter</span>
                <span>✅ One lowercase letter</span>
                <span>✅ One number</span>
                <span>✅ One special character</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("👥  Create Account"):
            if not full_name or not email or not phone or not password:
                st.markdown('<div class="error-box">Please fill all fields.</div>', unsafe_allow_html=True)
            else:
                payload = {
                    "full_name": full_name,
                    "email": email,
                    "phone": phone,
                    "password": password,
                    "role": role
                }

                try:
                    res = requests.post(f"{API_BASE_URL}/auth/register", json=payload)

                    if res.status_code == 200:
                        st.markdown(
                            '<div class="success-box">Account created successfully. Please login.</div>',
                            unsafe_allow_html=True
                        )
                    else:
                        st.markdown(
                            f'<div class="error-box">{res.json().get("detail", "Registration failed")}</div>',
                            unsafe_allow_html=True
                        )
                except requests.exceptions.ConnectionError:
                    st.markdown('<div class="error-box">Backend server is not running.</div>', unsafe_allow_html=True)

        st.markdown('<div class="bottom-link">Already have an account?</div>', unsafe_allow_html=True)

        if st.button("Go to Login"):
            st.session_state.page = "Login"
            st.rerun()

    elif page == "Login":
        st.markdown('<div class="form-icon">🔒</div>', unsafe_allow_html=True)
        st.markdown('<div class="main-title">Welcome Back</div>', unsafe_allow_html=True)
        st.markdown('<div class="main-subtitle">Login to continue to Smart CA</div>', unsafe_allow_html=True)
        st.markdown('<div class="title-line"></div>', unsafe_allow_html=True)

        email = st.text_input("Email Address", placeholder="Enter your email")
        password = st.text_input("Password", type="password", placeholder="Enter your password")

        if st.button("🔒  Login"):
            try:
                res = requests.post(
                    f"{API_BASE_URL}/auth/login",
                    json={"email": email, "password": password}
                )

                if res.status_code == 200:
                    data = res.json()
                    st.session_state.access_token = data.get("access_token")
                    st.session_state.refresh_token = data.get("refresh_token")
                    st.session_state.user = data.get("user")
                    st.session_state.page = "My Profile"
                    st.rerun()
                else:
                    st.markdown(
                        f'<div class="error-box">{res.json().get("detail", "Login failed")}</div>',
                        unsafe_allow_html=True
                    )
            except requests.exceptions.ConnectionError:
                st.markdown('<div class="error-box">Backend server is not running.</div>', unsafe_allow_html=True)

    elif page == "My Profile":
        st.markdown('<div class="form-icon">👤</div>', unsafe_allow_html=True)
        st.markdown('<div class="main-title">My Profile</div>', unsafe_allow_html=True)
        st.markdown('<div class="title-line"></div>', unsafe_allow_html=True)

        if not st.session_state.access_token:
            st.markdown('<div class="info-box">Please login first.</div>', unsafe_allow_html=True)
        else:
            res = requests.get(f"{API_BASE_URL}/auth/me", headers=auth_headers())

            if res.status_code == 200:
                user = res.json()
                st.markdown(f"""
                <div class="profile-card">
                    <h3>{user.get("full_name")}</h3>
                    <p><b>Email:</b> {user.get("email")}</p>
                    <p><b>Phone:</b> {user.get("phone")}</p>
                    <p><b>Role ID:</b> {user.get("role_id")}</p>
                    <p><b>Status:</b> {"Active" if user.get("is_active") else "Inactive"}</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(
                    f'<div class="error-box">{res.json().get("detail", "Unable to fetch profile")}</div>',
                    unsafe_allow_html=True
                )

    elif page == "Logout":
        st.markdown('<div class="form-icon">↪️</div>', unsafe_allow_html=True)
        st.markdown('<div class="main-title">Logout Current Device</div>', unsafe_allow_html=True)
        st.markdown('<div class="title-line"></div>', unsafe_allow_html=True)

        if not st.session_state.refresh_token:
            st.markdown('<div class="info-box">You are not logged in.</div>', unsafe_allow_html=True)
        else:
            if st.button("Logout Current Device"):
                res = requests.post(
                    f"{API_BASE_URL}/auth/logout",
                    json={"refresh_token": st.session_state.refresh_token}
                )

                if res.status_code == 200:
                    st.session_state.access_token = None
                    st.session_state.refresh_token = None
                    st.session_state.user = None
                    st.session_state.page = "Login"
                    st.rerun()
                else:
                    st.markdown(
                        f'<div class="error-box">{res.json().get("detail", "Logout failed")}</div>',
                        unsafe_allow_html=True
                    )

    elif page == "Logout All Devices":
        st.markdown('<div class="form-icon">📱</div>', unsafe_allow_html=True)
        st.markdown('<div class="main-title">Logout All Devices</div>', unsafe_allow_html=True)
        st.markdown('<div class="title-line"></div>', unsafe_allow_html=True)

        if not st.session_state.access_token:
            st.markdown('<div class="info-box">Please login first.</div>', unsafe_allow_html=True)
        else:
            st.warning("This will logout your account from all active devices.")

            if st.button("Logout From All Devices"):
                res = requests.post(
                    f"{API_BASE_URL}/auth/logout-all",
                    headers=auth_headers()
                )

                if res.status_code == 200:
                    st.session_state.access_token = None
                    st.session_state.refresh_token = None
                    st.session_state.user = None
                    st.session_state.page = "Login"
                    st.rerun()
                else:
                    st.markdown(
                        f'<div class="error-box">{res.json().get("detail", "Logout all failed")}</div>',
                        unsafe_allow_html=True
                    )

    elif page == "About":
        st.markdown('<div class="form-icon">💼</div>', unsafe_allow_html=True)
        st.markdown('<div class="main-title">About Smart CA</div>', unsafe_allow_html=True)
        st.markdown('<div class="title-line"></div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="profile-card">
            <h3>AI Powered Financial Advisor</h3>
            <p>Smart CA helps users with secure financial profile management, analytics, tax planning, document processing, and CA review workflows.</p>
        </div>
        """, unsafe_allow_html=True)

