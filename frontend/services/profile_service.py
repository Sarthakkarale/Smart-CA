from services.api import APIClient


class ProfileService:

    @staticmethod
    def create_profile(profile_data, token):

        return APIClient.post(
            "/profile/create",
            data=profile_data,
            token=token
        )

    @staticmethod
    def get_profile(token):

        return APIClient.get(
            "/profile/me",
            token=token
        )

    @staticmethod
    def update_profile(profile_data, token):

        return APIClient.put(
            "/profile/update",
            data=profile_data,
            token=token
        )

    @staticmethod
    def delete_profile(token):

        return APIClient.delete(
            "/profile/delete",
            token=token
        )