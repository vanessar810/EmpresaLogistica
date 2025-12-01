import pytest
from fastapi import HTTPException
from app.auth.auth_service import AuthService, pwd_context
from app.auth.auth_dto import UserCreate, UserLogin
from app.auth.jwt_utils import create_access_token


class FakeUser:
    def __init__(self, username, email, hashed_password):
        self.username = username
        self.email = email
        self.hashed_password = hashed_password


class FakeUserRepository:
    existing_user = None
    saved_user = None

    @classmethod
    def find_by_username(cls, db, username):
        if cls.existing_user and cls.existing_user.username == username:
            return cls.existing_user
        return None

    @classmethod
    def save(cls, db, user):
        cls.saved_user = user
        return user


def test_register_new_user(monkeypatch, db_session):
    # Mock repositorio y token
    monkeypatch.setattr("app.auth.auth_service.UserRepository", FakeUserRepository)
    monkeypatch.setattr("app.auth.auth_service.create_access_token", lambda data: "fake.jwt.token")

    # Datos del nuevo usuario
    user_data = UserCreate(username="vanessa", email="vanessa@test.com", password="12345")

    token = AuthService.register(user_data, db_session)

    assert token.access_token == "fake.jwt.token"
    assert FakeUserRepository.saved_user.username == "vanessa"
    assert pwd_context.verify("12345", FakeUserRepository.saved_user.hashed_password)


def test_register_existing_user(monkeypatch, db_session):
    FakeUserRepository.existing_user = FakeUser("vanessa", "vanessa@test.com", "hashed")
    monkeypatch.setattr("app.auth.auth_service.UserRepository", FakeUserRepository)

    user_data = UserCreate(username="vanessa", email="v@test.com", password="123")

    with pytest.raises(HTTPException) as exc:
        AuthService.register(user_data, db_session)
    assert exc.value.status_code == 400
    assert "El usuario ya se encuentra registrado." in str(exc.value.detail)


def test_login_valid_credentials(monkeypatch, db_session):
    user = FakeUser("vanessa", "v@test.com", pwd_context.hash("12345"))
    FakeUserRepository.existing_user = user

    monkeypatch.setattr("app.auth.auth_service.UserRepository", FakeUserRepository)
    monkeypatch.setattr("app.auth.auth_service.create_access_token", lambda data: "fake.jwt.token")

    credentials = UserLogin(username="vanessa", password="12345")
    token = AuthService.login(credentials, db_session)

    assert token.access_token == "fake.jwt.token"


def test_login_invalid_password(monkeypatch, db_session):
    user = FakeUser("vanessa", "v@test.com", pwd_context.hash("correct"))
    FakeUserRepository.existing_user = user
    monkeypatch.setattr("app.auth.auth_service.UserRepository", FakeUserRepository)

    credentials = UserLogin(username="vanessa", password="wrong")

    with pytest.raises(HTTPException) as exc:
        AuthService.login(credentials, db_session)
    assert exc.value.status_code == 401
    assert "Credenciales incorrectas. Verifica usuario o contraseña." in str(exc.value.detail)