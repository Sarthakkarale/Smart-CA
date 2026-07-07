import requests
import streamlit as st

# IMPORTANT: If your main.py includes routers with an "/api" prefix, add it here.
# Otherwise, leave it as localhost:8000
API_BASE_URL = "http://localhost:8000" 

class ProfileService:
    
    @staticmethod
    def create_profile(payload: dict):
        try:
            token = st.session_state.get("access_token", "")
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}"
            }
            
            response = requests.post(
                f"{API_BASE_URL}/profile/create", # <--- FIXED: Added /create
                json=payload, 
                headers=headers,
                timeout=10
            )
            return response
        except requests.exceptions.RequestException:
            return None
            
    @staticmethod
    def get_profile():
        try:
            token = st.session_state.get("access_token", "")
            headers = {"Authorization": f"Bearer {token}"}
            
            response = requests.get(
                f"{API_BASE_URL}/profile/me", # This one was already correct based on your router!
                headers=headers,
                timeout=5
            )
            return response
        except requests.exceptions.RequestException:
            return None