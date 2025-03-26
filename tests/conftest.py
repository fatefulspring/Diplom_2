import pytest
import requests

from helpers.data import USER_LOGIN_URL, USER_REGISTRATION_URL
from helpers.utils import generate_registration_data


@pytest.fixture
def new_user():
    email, password, name = generate_registration_data()
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    response = requests.post(USER_REGISTRATION_URL, data=payload)
    return response, email, password, name

@pytest.fixture
def access_token(new_user):
    _, email, password, _ = new_user
    payload = {
        "email": email,
        "password": password
    }
    response = requests.post(USER_LOGIN_URL, data=payload)
    return response.json()['accessToken']
