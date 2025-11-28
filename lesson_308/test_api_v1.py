# api testing
import requests

# https://github.com/alex-pancho/car_service_api_and_ui

base_url = "http://127.0.0.1:8000/api"

def test_sigin_positive():
    endpoint = "/auth/signin/"
    data = {
    "username": "admin",
    "password": "QWas12"
    }

    response = requests.post(base_url+endpoint, json=data)
    #response.raise_for_status()
    r_json = response.json()

    assert r_json.get("access") is not None, f"Hasn`t 'access' key: {r_json}"
    assert r_json.get("refresh") is not None, f"Hasn`t 'refresh' key {r_json}"

def test_sigin_negative():
    endpoint = "/auth/signin/"
    data = {
    "username": "admin",
    "password": "QWas123"
    }

    response = requests.post(base_url+endpoint, json=data)
    r_json = response.json()

    assert r_json.get("detail") is not None, f"Hasn`t 'detail' key: {r_json}"

def test_refresh_positive():
    endpoint = "/auth/signin/"
    data = {
    "username": "admin",
    "password": "QWas12"
    }

    response = requests.post(base_url+endpoint, json=data)
    response.raise_for_status()
    r_json = response.json()
    refresh_token = r_json.get("refresh")
    access_token = r_json.get("access")
    assert access_token is not None, f"Hasn`t 'access' key: {r_json}"
    assert refresh_token is not None, f"Hasn`t 'refresh' key {r_json}"

    endpoint = "/auth/token/refresh/"
    data = {
        "refresh": refresh_token
        }
    response = requests.post(base_url+endpoint, json=data)
    response.raise_for_status()
    r_json = response.json()
    new_refresh_token = r_json.get("refresh")
    new_access_token = r_json.get("access")
    assert new_access_token != access_token
    assert new_refresh_token != refresh_token

