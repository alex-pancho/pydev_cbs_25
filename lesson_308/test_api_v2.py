import requests
from car_api import API

api = API()

s = requests.Session()

def test_sigin_positive():
    
    data = {
    "username": "admin",
    "password": "QWas12"
    }

    response = api.auth.signin(s, data, json=False)
    response.raise_for_status()
    r_json = response.json()

    assert r_json.get("access") is not None, f"Hasn`t 'access' key: {r_json}"
    assert r_json.get("refresh") is not None, f"Hasn`t 'refresh' key {r_json}"

def test_sigin_negative():

    data = {
    "username": "admin",
    "password": "QWas123"
    }

    r_json = api.auth.signin(s, data)

    assert r_json.get("detail") is not None, f"Hasn`t 'detail' key: {r_json}"

def test_refresh_positive():

    data = {
    "username": "admin",
    "password": "QWas12"
    }

    r_json = api.auth.signin(s, data)
 
    refresh_token = r_json.get("refresh")
    access_token = r_json.get("access")
    assert access_token is not None, f"Hasn`t 'access' key: {r_json}"
    assert refresh_token is not None, f"Hasn`t 'refresh' key {r_json}"

    
    data = {
        "refresh": refresh_token
        }
    r_json = api.auth.token_refresh(s, data)
    
    new_refresh_token = r_json.get("refresh")
    new_access_token = r_json.get("access")
    assert new_access_token != access_token
    assert new_refresh_token != refresh_token

def test_car(get_auth_user):
    s = get_auth_user
    r_json = api.cars.cars_get(s)
    assert r_json.get("count") is not None, r_json