import allure
import requests

from helpers.data import USER_LOGIN_URL

from . import constants


class TestLogin:

    @allure.title("Логин пользователя с корректными данными")
    def test_login_user(self, new_user):
        _, email, password, _ = new_user
        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(USER_LOGIN_URL, data=payload)
        assert response.status_code == 200
        assert sorted(['accessToken', 'refreshToken', 'success', 'user']) == sorted(response.json().keys())

    @allure.title("Логин пользователя с некорректными данными")
    def test_login_user_incorrect_data(self):
        payload = {
            "email": 'email@example.com',
            "password": 'password'
        }
        response = requests.post(USER_LOGIN_URL, data=payload)
        assert response.status_code == 401
        assert response.json()['message'] == constants.INCORRECT_EMAIL
