"""
API Configuration
-----------------
Centralized backend configuration for Smart CA.
All API requests should use this file.
"""

# ==========================================================
# Backend Configuration
# ==========================================================

BASE_URL = "http://127.0.0.1:8000"

# ==========================================================
# Authentication Endpoints
# ==========================================================

AUTH_BASE = f"{BASE_URL}/auth"

LOGIN_URL = f"{AUTH_BASE}/login"

REGISTER_URL = f"{AUTH_BASE}/register"

LOGOUT_URL = f"{AUTH_BASE}/logout"

REFRESH_TOKEN_URL = f"{AUTH_BASE}/refresh"

ME_URL = f"{AUTH_BASE}/me"

# ==========================================================
# Default Request Timeout (seconds)
# ==========================================================

REQUEST_TIMEOUT = 15

# ==========================================================
# Default Headers
# ==========================================================

DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}