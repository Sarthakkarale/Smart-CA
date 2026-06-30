from services.api import APIClient


class DashboardService:

    @staticmethod
    def get_profile(token):

        return APIClient.get(
            "/profile/me",
            token=token
        )