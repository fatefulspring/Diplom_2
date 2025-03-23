import allure
import requests

from helpers.data import USER_AUTH_URL
from helpers.utils import register_and_login


class TestLogin:

    @allure.title("Изменение данных пользователя с авторизацией")
    def test_user_change_data(self):
        token = register_and_login()
        payload = {
            "name": "NewName"
        }
        headers = {
            "Authorization": token
        }
        response = requests.patch(USER_AUTH_URL, headers=headers, data=payload)
        assert response.status_code == 200
        assert response.json()['user']['name'] == "NewName"

    @allure.title("Изменение данных пользователя без авторизации")
    def test_user_change_data_without_auth(self):
        _ = register_and_login()
        payload = {
            "name": "NewName"
        }
        headers = {
            "Authorization": "token123"
        }
        response = requests.patch(USER_AUTH_URL, headers=headers, data=payload)
        assert response.status_code == 401
        assert response.json()['message'] == "You should be authorised"
