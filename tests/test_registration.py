import allure
import requests

from helpers.data import USER_REGISTRATION_URL
from helpers.utils import generate_registration_data


class TestRegistration:

    @allure.title("Регистрация нового пользователя")
    def test_registration_new_user(self):
        email, password, name = generate_registration_data()
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(USER_REGISTRATION_URL, data=payload)
        assert response.status_code == 200
        assert sorted(['accessToken', 'refreshToken', 'success', 'user']) == sorted(response.json().keys())

    @allure.title("Регистрация пользователя, если такой пользователь уже существует")
    def test_registration_duplicate_user(self):
        payload = {
            "email": "test_email@asd.asd",
            "password": "test_password",
            "name": "test_name"
        }
        response = requests.post(USER_REGISTRATION_URL, data=payload)
        assert response.status_code == 403
        assert response.json()['message'] == 'User already exists'


    @allure.title("Логин с пустыми полями")
    def test_registration_user(self):
        payload = {}
        response = requests.post(USER_REGISTRATION_URL, data=payload)
        assert response.status_code == 403
        assert response.json()['message'] == 'Email, password and name are required fields'
