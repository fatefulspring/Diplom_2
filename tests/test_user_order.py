import allure
import requests

from helpers.data import USER_ORDERS_URL

from . import constants


class TestLogin:

    @allure.title("Получение заказа авторизованного пользователя")
    def test_auth_user_order(self, access_token):
        headers = {
            "Authorization": access_token
        }
        response = requests.get(USER_ORDERS_URL, headers=headers)
        assert response.status_code == 200
        assert sorted(['success', 'orders', 'total', 'totalToday']) == sorted(response.json().keys())

    @allure.title("Получение заказа неавторизованного пользователя")
    def test_not_auth_user_order(self):
        response = requests.get(USER_ORDERS_URL)
        assert response.status_code == 401
        assert response.json()['message'] == constants.AUTH_ERROR
