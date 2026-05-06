import requests
import time

class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None

    def login(self, email, password):
        url = f"{self.base_url}/users/login"

        payload = {
            "email": email,
            "password": password
        }

        res = requests.post(url, json=payload)

        assert res.status_code == 200, "Login API failed"

        self.token = res.json()["data"]["token"]

    def _headers(self):
        return {
            "x-auth-token": self.token
        }

    def get_notes(self):
        url = f"{self.base_url}/notes"

        start = time.time()
        res = requests.get(url, headers=self._headers())
        end = time.time()

        response_time = end - start

        assert res.status_code == 200

        return res.json(), response_time