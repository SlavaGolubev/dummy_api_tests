import allure
import requests


class BaseClient:
    def __init__(self, base_url: str = "https://dummyjson.com"):
        self.base_url = base_url
        self.session = requests.Session()  # Создаем сессию ОДИН раз

    def _request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        with allure.step(f"{method} {endpoint}"):
            response = self.session.request(method=method, url=url, **kwargs)
            allure.attach(
                response.text,
                name=f"Response [{response.status_code}]",
                attachment_type=allure.attachment_type.JSON,
            )
            return response

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        return self._request("DELETE", endpoint, **kwargs)