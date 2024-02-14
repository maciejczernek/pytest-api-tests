import os
import requests
import allure


class JsonPlaceholder:
    BASE_URL = "https://jsonplaceholder.typicode.com/"

    def __init__(self):
        self.timeout = 5

    @allure.step("GET resource")
    def get_resource(self, id):
        url = os.path.join(self.BASE_URL, f"posts/{id}")
        allure.attach(url, "url")
        return requests.get(url, timeout=self.timeout)

    @allure.step("GET all resources")
    def get_all_resource(self):
        url = os.path.join(self.BASE_URL, f"posts")
        allure.attach(url, "url")
        return requests.get(url, timeout=self.timeout)

    @allure.step("DELETE resource")
    def delete_resource(self, id):
        url = os.path.join(self.BASE_URL, f"posts/{id}")
        allure.attach(url, "url")
        return requests.delete(url, timeout=self.timeout)

    @allure.step("POST resource")
    def post_resource(self, data):
        url = os.path.join(self.BASE_URL, f"posts")
        allure.attach(url, "url")
        return requests.post(url, data=data, timeout=self.timeout)
