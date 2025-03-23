import allure
import requests

from helpers.data import INGREDIENTS, INVALID_INGREDIENTS, USER_ORDERS_URL
from helpers.utils import register_and_login


class TestLogin:

    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_add_order_with_auth_and_with_ingredients(self):
        token = register_and_login()
        payload = {"ingredients": INGREDIENTS}
        headers = {
            "Authorization": token
        }
        response = requests.post(USER_ORDERS_URL, headers=headers, data=payload)
        assert sorted(['name', 'order', 'success']) == sorted(response.json().keys())

    @allure.title("Создание заказа без авторизации")
    def test_add_order_without_auth(self):
        payload = {"ingredients": INGREDIENTS}
        response = requests.post(USER_ORDERS_URL, data=payload)
        assert sorted(['name', 'order', 'success']) == sorted(response.json().keys())

    @allure.title("Создание заказа без ингредиентов")
    def test_add_order_without_ingredients(self):
        payload = {"ingredients": []}
        response = requests.post(USER_ORDERS_URL, data=payload)
        assert response.status_code == 400
        assert response.json()['message'] == 'Ingredient ids must be provided'

    @allure.title("Создание заказа с невалидным хешем ингредиентов")
    def test_add_order_invalid_hash(self):
        payload = {"ingredients": INVALID_INGREDIENTS}
        response = requests.post(USER_ORDERS_URL, data=payload)
        assert response.status_code == 500
