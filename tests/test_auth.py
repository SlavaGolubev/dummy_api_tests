import pytest
from api.auth_api import AuthAPI
from models.auth_models import ErrorResponse, LoginResponse, UserMeResponse


class TestAuth:
    def test_login_success(self, auth_api: AuthAPI):
        response = auth_api.login("emilys", "emilyspass")
        assert response.status_code == 200

        # Валидируем структуру и типы всех полей ответа одной строкой
        user_data = LoginResponse(**response.json())
        assert user_data.username == "emilys"
        assert user_data.accessToken != ""

    @pytest.mark.parametrize(
        "username, password",
        [
            ("emilys", "wrong_pass"),
            ("unknown_user", "emilyspass"),
            (None, "emilyspass"),
            ("emilys", None),
        ],
    )
    def test_login_negative(self, auth_api: AuthAPI, username, password):
        response = auth_api.login(username=username, password=password)
        assert response.status_code == 400
        ErrorResponse(**response.json())  # Проверяем, что пришла ошибка с полем message

    def test_get_me_success(self, auth_api: AuthAPI, auth_token: str):
        response = auth_api.get_me(token=auth_token)
        assert response.status_code == 200

        profile = UserMeResponse(**response.json())
        assert profile.username == "emilys"

    @pytest.mark.parametrize("token", [None, "invalid_token_123"])
    def test_get_me_unauthorized(self, auth_api: AuthAPI, token):
        response = auth_api.get_me(token=token)
        assert response.status_code == 401
