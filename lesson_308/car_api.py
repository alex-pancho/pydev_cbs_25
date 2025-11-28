from requests import Session
base_api_url = "http://127.0.0.1:8000/api"

from functools import wraps

class jsonreturn(staticmethod):

    def __init__(self, func):
        super().__init__(func)
        self.func = func     # зберігаємо оригінальну функцію

    def __get__(self, instance, owner):
        # отримуємо функцію як staticmethod робить сам
        original = super().__get__(instance, owner)

        def wrapper(*args, json=True, **kwargs):
            resp = original(*args, **kwargs)
            if json:
                try:
                    return resp.json()
                except Exception:
                    return {
                        "status_code": resp.status_code,
                        "text": resp.text,
                        "error": "Non-JSON response"
                    }
            return resp

        return wrapper


class Auth():

    @staticmethod
    def _return(resp, json: bool):
        if json:
            try:
                return resp.json()
            except ValueError:
                return {
                    "status_code": resp.status_code,
                    "text": resp.text,
                    "error": "Non-JSON response"
                }
        return resp

    @staticmethod
    def logout(s: Session, request_body: dict = {}, json: bool = True):
        endpoint = "/auth/logout"
        resp = s.post(f"{base_api_url}{endpoint}/")
        return Auth._return(resp, json)

    @jsonreturn
    def signup(s: Session, request_body: dict):
        """
        
        Args:
            s: Session
        """
        endpoint = "/auth/signup"
        return s.post(f"{base_api_url}{endpoint}/", json=request_body)

    @jsonreturn
    def signin(s: Session, request_body: dict):
        endpoint = "/auth/signin"
        return s.post(f"{base_api_url}{endpoint}/", json=request_body)

    @jsonreturn
    def reset_password(s: Session, request_body: dict):
        endpoint = "/auth/resetpassword"
        return s.post(f"{base_api_url}{endpoint}/", json=request_body)

    @jsonreturn
    def token_refresh(s: Session, request_body: dict):
        endpoint = "/auth/token/refresh"
        return s.post(f"{base_api_url}{endpoint}/", json=request_body)

class Users():

    @jsonreturn
    def current(s: Session, request_body: dict = {}):
        endpoint = "/users/current"
        return s.get(f"{base_api_url}{endpoint}/")

    @jsonreturn
    def profile_get(s: Session, request_body: dict = {}):
        endpoint = "/users/profile"
        return s.get(f"{base_api_url}{endpoint}/")

    @jsonreturn
    def profile_put(s: Session, request_body: dict):
        endpoint = "/users/profile"
        return s.put(f"{base_api_url}{endpoint}/", json=request_body)

    @jsonreturn
    def settings_get(s: Session, request_body: dict = {}):
        endpoint = "/users/settings"
        return s.get(f"{base_api_url}{endpoint}/")

    @jsonreturn
    def settings_put(s: Session, request_body: dict):
        endpoint = "/users/settings"
        return s.put(f"{base_api_url}{endpoint}/", json=request_body)

    @jsonreturn
    def resetpassword(s:Session, user_id:int, token:str):
        # TODO: make this part better
        endpoint = f"/users/resetpassword/{user_id}/{token}"
        return s.get(f"{base_api_url}{endpoint}/")

    @jsonreturn
    def email(s: Session, request_body: dict):
        endpoint = "/users/email"
        return s.put(f"{base_api_url}{endpoint}/", json=request_body)

    @jsonreturn
    def password(s: Session, request_body: dict):
        endpoint = "/users/password"
        return s.put(f"{base_api_url}{endpoint}/", json=request_body)

    @jsonreturn
    def users(s: Session, request_body: dict = {}):
        endpoint = "/users"
        return s.delete(f"{base_api_url}{endpoint}/")


class Cars():
    @jsonreturn
    def brands(s: Session, request_body: dict = {}):
        endpoint = "/cars/brands"
        return s.get(f"{base_api_url}{endpoint}/")

    @jsonreturn
    def brands_id(s: Session, request_body: dict):
        id_ = request_body.get("id", 0)
        endpoint = f"/cars/brands/{id_}"
        return s.get(f"{base_api_url}{endpoint}/")

    @jsonreturn
    def models(s: Session, request_body: dict = {}):
        endpoint = "/cars/models"
        return s.get(f"{base_api_url}{endpoint}/")

    @jsonreturn
    def models_id(s: Session, request_body: dict):
        id_ = request_body.get("id", 0)
        endpoint = f"/cars/models/{id_}"
        return s.get(f"{base_api_url}{endpoint}/")

    @jsonreturn
    def cars_get(s: Session, request_body: dict = {}):
        endpoint = "/cars"
        return s.get(f"{base_api_url}{endpoint}/")

    @jsonreturn
    def cars_post(s: Session, request_body: dict):
        endpoint = "/cars"
        return s.post(f"{base_api_url}{endpoint}/", json=request_body)

    @jsonreturn
    def cars_id_get(s: Session, request_body: dict):
        id_ = request_body.get("id", 0)
        endpoint = f"/cars/{id_}"
        return s.get(f"{base_api_url}{endpoint}/")

    @jsonreturn
    def cars_id_put(s: Session, request_body: dict):
        id_ = request_body.pop("id", 0)
        endpoint = f"/cars/{id_}"
        return s.put(f"{base_api_url}{endpoint}/", json=request_body)

    @jsonreturn
    def cars_id_delete(s: Session, request_body: dict):
        id_ = request_body.get("id", 0)
        endpoint = f"/cars/{id_}"
        return s.delete(f"{base_api_url}{endpoint}/")


class Expenses():

    @jsonreturn
    def expenses_get(s: Session, request_body: dict):
        car_id = request_body.get("id", 0)
        page = request_body.get("page", 0)
        endpoint = "/expenses"
        query = {"carId": car_id, "page": page}
        return s.get(f"{base_api_url}{endpoint}/", params=query)

    @jsonreturn
    def expenses_post(s: Session, request_body: dict):
        endpoint = "/expenses"
        return s.post(f"{base_api_url}{endpoint}/", json=request_body)

    @jsonreturn
    def expenses_id_get(s: Session, request_body: dict):
        id_ = request_body.get("id", 1)
        endpoint = f"/expenses/{id_}"
        return s.get(f"{base_api_url}{endpoint}/")

    @jsonreturn
    def expenses_id_put(s: Session, request_body: dict):
        id_ = request_body.pop("id") if request_body.get("id") is not None else request_body.get("carId", 1)
        endpoint = f"/expenses/{id_}"
        return s.put(f"{base_api_url}{endpoint}/", json=request_body)

    @jsonreturn
    def expenses_id_delete(s: Session, request_body: dict):
        id_ = request_body.get("id", 1)
        endpoint = f"/expenses/{id_}"
        return s.delete(f"{base_api_url}{endpoint}/")


class Instructions():

    @jsonreturn
    def instructions(s: Session, request_body: dict):
        car_brand_id = request_body.get("carBrandId", 0)
        car_model_id = request_body.get("carModelId", 0)
        page = request_body.get("page", 0)
        endpoint = "/instructions"
        query = {"carBrandId": car_brand_id,
                 "carModelId": car_model_id,
                 "page": page}
        return s.get(f"{base_api_url}{endpoint}/", params=query)

    @jsonreturn
    def instructions_id(s: Session, request_body: dict):
        id_ = request_body.get("id", 1)
        endpoint = f"/instructions/{id_}"
        return s.get(f"{base_api_url}{endpoint}/")


class API():
    auth = Auth()
    users = Users()
    cars = Cars()
    expenses = Expenses()
    instructions = Instructions()