import random
import string

import requests

from .data import USER_LOGIN_URL, USER_REGISTRATION_URL


def generate_registration_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    email = f'{generate_random_string(10)}@{generate_random_string(3)}.{generate_random_string(3)}'
    password = generate_random_string(10)
    name = generate_random_string(10)


    return email, password, name

# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_user():
    email, password, name = generate_registration_data()
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    response = requests.post(USER_REGISTRATION_URL, data=payload)
    return response, email, password, name

def register_and_login():
    _, email, password, _ = register_new_user()
    payload = {
        "email": email,
        "password": password
    }
    response = requests.post(USER_LOGIN_URL, data=payload)
    return response.json()['accessToken']
