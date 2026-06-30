import requests

# =====================================
# Backend Configuration
# =====================================

BASE_URL = "http://127.0.0.1:8000"


# =====================================
# API Client
# =====================================

class APIClient:

    @staticmethod
    def get(endpoint, token=None):

        headers = {}

        if token:
            headers["Authorization"] = f"Bearer {token}"

        response = requests.get(
            BASE_URL + endpoint,
            headers=headers
        )

        return response

    @staticmethod
    def post(endpoint, data=None, token=None):

        headers = {
            "Content-Type": "application/json"
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        response = requests.post(
            BASE_URL + endpoint,
            json=data,
            headers=headers
        )

        return response

    @staticmethod
    def put(endpoint, data=None, token=None):

        headers = {
            "Content-Type": "application/json"
        }

        if token:
            headers["Authorization"] = f"Bearer {token}"

        response = requests.put(
            BASE_URL + endpoint,
            json=data,
            headers=headers
        )

        return response

    @staticmethod
    def delete(endpoint, token=None):

        headers = {}

        if token:
            headers["Authorization"] = f"Bearer {token}"

        response = requests.delete(
            BASE_URL + endpoint,
            headers=headers
        )

        return response