from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.auth.auth_dto import UserCreate, UserLogin, Token
from app.entity.user import User
from app.repository.user_repository import UserRepository
from app.auth.jwt_utils import create_access_token
from app.exception.http_exceptions import invalid_credentials, user_already_exists, internal_server_error

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

class AuthService:
    @staticmethod
    def register(user_data: UserCreate, db: Session):
        try:
            existing_user = UserRepository.find_by_username(db, user_data.username)
            if existing_user:
                raise user_already_exists()

            hashed_password = pwd_context.hash(user_data.password)
            user = User(
                username=user_data.username,
                email=user_data.email,
                hashed_password=hashed_password
            )
            UserRepository.save(db, user)
            access_token = create_access_token(data={"sub": user.username})
            return Token(access_token=access_token)

        except HTTPException:
            raise
        except Exception as e:
            print(f"❌ Error al registrar usuario: {e}")
            raise internal_server_error("No se pudo registrar el usuario.")

    @staticmethod
    def login(credentials: UserLogin, db: Session):
        try:
            user = UserRepository.find_by_username(db, credentials.username)
            if not user or not pwd_context.verify(credentials.password, user.hashed_password):
                raise invalid_credentials()

            access_token = create_access_token(data={"sub": user.username})
            return Token(access_token=access_token)

        except HTTPException:
            raise
        except Exception as e:
            print(f"❌ Error en login: {e}")
            raise internal_server_error("Error interno al iniciar sesión.")