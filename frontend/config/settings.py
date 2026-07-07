"""
Smart CA - Application Settings
--------------------------------

Central configuration for the Streamlit frontend.

This file should contain only application-level configuration
and constants that are reused across the project.

Sprint:
    Phase 1 (UI Foundation)

Author:
    Smart CA Frontend
"""

from pathlib import Path

# ==========================================================
# Application
# ==========================================================

APP_NAME: str = "Smart CA"

APP_ICON: str = "💼"

APP_VERSION: str = "1.0.0"

LAYOUT: str = "wide"

SIDEBAR_STATE: str = "collapsed"

# ==========================================================
# Backend
# ==========================================================

API_BASE_URL: str = "http://127.0.0.1:8000"

API_TIMEOUT: int = 30

# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

ASSETS_DIR = BASE_DIR / "assets"

CSS_FILE = ASSETS_DIR / ""

IMAGES_DIR = ASSETS_DIR / "images"

ICONS_DIR = ASSETS_DIR / "icons"

# ==========================================================
# Theme
# ==========================================================

PRIMARY_COLOR = "#6D5EF8"

BACKGROUND_COLOR = "#F5F7FB"

DARK_COLOR = "#111827"

TEXT_COLOR = "#1E293B"

SUBTITLE_COLOR = "#64748B"

SUCCESS_COLOR = "#10B981"

WARNING_COLOR = "#F59E0B"

DANGER_COLOR = "#EF4444"

CARD_RADIUS = 20

# ==========================================================
# Authentication
# ==========================================================

ACCESS_TOKEN_KEY = "access_token"

REFRESH_TOKEN_KEY = "refresh_token"

CURRENT_USER_KEY = "current_user"

# ==========================================================
# Navigation Pages
# ==========================================================

PAGE_LANDING = "landing"

PAGE_LOGIN = "login"

PAGE_REGISTER = "register"

PAGE_DASHBOARD = "dashboard"

PAGE_PROFILE = "profile"

PAGE_DOCUMENTS = "documents"

PAGE_ADVISOR = "advisor"

PAGE_REPORTS = "reports"

PAGE_SETTINGS = "settings"

PAGE_TAX = "tax"

# ==========================================================
# Default Landing Page
# ==========================================================

DEFAULT_PAGE = PAGE_LANDING