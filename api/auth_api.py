import requests
from api.base_client import BaseClient


class AuthAPI(BaseClient):
    def login(
        self,
        username: str | None = None,
        password: str | None = None,
        expires_in_mins: int | None = None,
    ) -> requests.Response:
        # Собираем словарь только из переданных (не None) полей
        raw_payload = {
            "username": username,
            "password": password,
            "expiresInMins": expires_in_mins,
        }
        payload = {k: v for k, v in raw_payload.items() if v is not None}
        return self.post("/auth/login", json=payload)

    def get_me(self, token: str | None = None) -> requests.Response:
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        return self.get("/auth/me", headers=headers)