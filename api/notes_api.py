import requests


class NotesAPI:

    def __init__(self, config):
        self.base_url = config["api_url"]
        self.email = config["email"]
        self.password = config["password"]
        self.token = None

    
    def login(self):
        url = f"{self.base_url}/users/login"

        payload = {
            "email": self.email,
            "password": self.password
        }

        response = requests.post(url, json=payload)
        data = response.json()

        self.token = data["data"]["token"]
        return self.token

    def headers(self):
        return {
            "x-auth-token": self.token
        }

    def get_notes(self):
        return requests.get(
            f"{self.base_url}/notes",
            headers=self.headers()
        )

    def create_note(self, title, description, category):
        return requests.post(
            f"{self.base_url}/notes",
            json={
                "title": title,
                "description": description,
                "category": category
            },
            headers=self.headers()
        )

    def update_note(self, note_id, title, description, category, completed=False):
        return requests.put(
            f"{self.base_url}/notes/{note_id}",
            json={
                "title": title,
                "description": description,
                "category": category,
                "completed": completed
            },
            headers=self.headers()
        )

    def delete_note(self, note_id):
        return requests.delete(
            f"{self.base_url}/notes/{note_id}",
            headers=self.headers()
        )