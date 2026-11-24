import pytest
from api.auth_api import AuthAPI
from api.products_api import ProductsApi


@pytest.fixture
def auth_api() -> AuthAPI:
    return AuthAPI()


@pytest.fixture
def auth_token(auth_api: AuthAPI) -> str:
    # Быстрая подготовка токена для тестов, которым нужен залогиненный юзер
    response = auth_api.login("emilys", "emilyspass")
    assert response.status_code == 200
    return response.json()["accessToken"]

@pytest.fixture
def products_api() -> ProductsApi:
    return ProductsApi()