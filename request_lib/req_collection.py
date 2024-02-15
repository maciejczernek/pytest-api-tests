import os
import requests
import allure

from tests.config import AllureConfig


class JsonPlaceholder:
    BASE_URL = "https://jsonplaceholder.typicode.com/"

    def __init__(self):
        self.timeout = 5
        self.allure_utils = AllureConfig()

    @allure.step("GET resource")
    def get_resource(self, id):
        url = os.path.join(self.BASE_URL, f"posts/{id}")
        r = requests.get(url, timeout=self.timeout)
        self.allure_utils.attach_info(r)
        return r

    @allure.step("GET all resources")
    def get_all_resource(self):
        url = os.path.join(self.BASE_URL, f"posts")
        r = requests.get(url, timeout=self.timeout)
        self.allure_utils.attach_info(r)
        return r

    @allure.step("DELETE resource")
    def delete_resource(self, id):
        url = os.path.join(self.BASE_URL, f"posts/{id}")
        r = requests.delete(url, timeout=self.timeout)
        self.allure_utils.attach_info(r)
        return r

    @allure.step("POST resource")
    def post_resource(self, data):
        url = os.path.join(self.BASE_URL, f"posts")
        r = requests.post(url, data=data, timeout=self.timeout)
        self.allure_utils.attach_info(r)
        return r
