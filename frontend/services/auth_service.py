"""
Authentication Service
----------------------
Handles all authentication API calls.
"""

import requests

from services.api import (
    LOGIN_URL,
    REGISTER_URL,
    LOGOUT_URL,
    ME_URL,
    REQUEST_TIMEOUT,
    DEFAULT_HEADERS,
)


class AuthService:
    """Authentication API Service"""

    @staticmethod
    def login(email: str, password: str) -> dict:
        """
        Authenticate user.
        """

        payload = {
            "email": email,
            "password": password,
        }

        try:

            response = requests.post(
                LOGIN_URL,
                json=payload,
                headers=DEFAULT_HEADERS,
                timeout=REQUEST_TIMEOUT,
            )

            data = response.json()

            if response.status_code == 200:
                return data

            return {
                "success": False,
                "message": data.get("detail", "Login failed."),
            }

        except requests.exceptions.ConnectionError:
            return {
                "success": False,
                "message": "Unable to connect to backend server.",
            }

        except requests.exceptions.Timeout:
            return {
                "success": False,
                "message": "Request timed out.",
            }

        except Exception as e:
            return {
                "success": False,
                "message": str(e),
            }

    @staticmethod
    def register(
        full_name: str,
        email: str,
        phone: str,
        password: str,
    ) -> dict:
        """
        Register new user.
        """

        payload = {
            "full_name": full_name,
            "email": email,
            "phone": phone,
            "password": password,
        }

        try:

            response = requests.post(
                REGISTER_URL,
                json=payload,
                headers=DEFAULT_HEADERS,
                timeout=REQUEST_TIMEOUT,
            )

            data = response.json()

            if response.status_code == 200:
                return data

            return {
                "success": False,
                "message": data.get("detail", "Registration failed."),
            }

        except requests.exceptions.ConnectionError:
            return {
                "success": False,
                "message": "Unable to connect to backend server.",
            }

        except requests.exceptions.Timeout:
            return {
                "success": False,
                "message": "Request timed out.",
            }

        except Exception as e:
            return {
                "success": False,
                "message": str(e),
            }

    @staticmethod
    def get_current_user(access_token: str) -> dict:
        """
        Get logged-in user details.
        """

        headers = {
            **DEFAULT_HEADERS,
            "Authorization": f"Bearer {access_token}",
        }

        try:

            response = requests.get(
                ME_URL,
                headers=headers,
                timeout=REQUEST_TIMEOUT,
            )

            return response.json()

        except Exception as e:

            return {
                "success": False,
                "message": str(e),
            }

    @staticmethod
    def logout(refresh_token: str) -> dict:
        """
        Logout user.
        """

        payload = {
            "refresh_token": refresh_token,
        }

        try:

            response = requests.post(
                LOGOUT_URL,
                json=payload,
                headers=DEFAULT_HEADERS,
                timeout=REQUEST_TIMEOUT,
            )

            return response.json()

        except Exception as e:

            return {
                "success": False,
                "message": str(e),
            }