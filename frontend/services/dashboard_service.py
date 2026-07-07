import requests
import streamlit as st

API_BASE_URL = "http://localhost:8000"

class DashboardService:
    @staticmethod
    def _get_headers():
        token = st.session_state.get("access_token", "")
        return {"Authorization": f"Bearer {token}"}

    @staticmethod
    def get_summary():
        try:
            return requests.get(f"{API_BASE_URL}/dashboard/summary", headers=DashboardService._get_headers(), timeout=5)
        except requests.exceptions.RequestException:
            return None

    @staticmethod
    def get_ai_suggestions():
        try:
            return requests.get(f"{API_BASE_URL}/dashboard/ai-suggestions", headers=DashboardService._get_headers(), timeout=5)
        except requests.exceptions.RequestException:
            return None

    @staticmethod
    def get_charts():
        try:
            return requests.get(f"{API_BASE_URL}/dashboard/charts", headers=DashboardService._get_headers(), timeout=5)
        except requests.exceptions.RequestException:
            return None
            
    @staticmethod
    def get_profile_summary():
        try:
            return requests.get(f"{API_BASE_URL}/dashboard/profile-summary", headers=DashboardService._get_headers(), timeout=5)
        except requests.exceptions.RequestException:
            return None