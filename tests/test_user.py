import allure
import requests

from helpers.data import USER_AUTH_URL

from . import constants


class TestLogin:

    @allure.title("Изменение данных пользователя с авторизацией")
    def test_user_change_data(self, access_token):
        payload = {
            "name": constants.NEW_NAME
        }
        headers = {
            "Authorization": access_token
        }
        response = requests.patch(USER_AUTH_URL, headers=headers, data=payload)
        assert response.status_code == 200
        assert response.json()['user']['name'] == constants.NEW_NAME

    @allure.title("Изменение данных пользователя без авторизации")
    def test_user_change_data_without_auth(self, new_user):
        payload = {
            "name": constants.NEW_NAME
        }
        headers = {
            "Authorization": constants.INVALID_TOKEN
        }
        response = requests.patch(USER_AUTH_URL, headers=headers, data=payload)
        assert response.status_code == 401
        assert response.json()['message'] == constants.AUTH_ERROR
