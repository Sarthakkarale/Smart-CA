import requests

API_BASE_URL = "http://localhost:8000" # Update this if your backend runs on a different port/path

class AuthService:
    
    @staticmethod
    def login(email: str, password: str):
        try:
            # Sending as standard JSON for your Pydantic model
            payload = {
                "email": email, 
                "password": password
            }
            
            response = requests.post(
                f"{API_BASE_URL}/auth/login", 
                json=payload,  # <-- Changed from data=payload to json=payload
                timeout=10
            )
            return response
        except requests.exceptions.RequestException:
            return None

    @staticmethod
    def register(full_name: str, email: str, password: str):
        try:
            payload = {
                "full_name": full_name,
                "email": email,
                "password": password
            }
            
            response = requests.post(
                f"{API_BASE_URL}/auth/register", # Adjust endpoint path to match your FastAPI router
                json=payload, 
                timeout=10
            )
            return response
        except requests.exceptions.RequestException:
            return None