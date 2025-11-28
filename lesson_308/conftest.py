import pytest
import requests
from car_api import API

api = API()

s = requests.Session()

@pytest.fixture()
def get_auth_user():
    # приєднуємося
    data = {
    "username": "admin",
    "password": "QWas12"
    }

    response = api.auth.signin(s, data)
    headers = {
        "Authorization": f"Bearer {response.get('access')}", 
        "refresh": response.get('refresh')}
    s.headers.update(headers)
    yield s
    # чистимо і відєднуємся
    response = api.auth.logout(s)
    print(response)