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
            existing_user = UserRepository.find_by_email(db, user_data.email)
            if existing_user:
                raise user_already_exists()

            hashed_password = pwd_context.hash(user_data.password)
            user = User(
                email=user_data.email,
                hashed_password=hashed_password,
                role=user_data.role
            )
            UserRepository.save(db, user)
            access_token = create_access_token(data={"sub": user.email})
            has_client = bool(user.cliente)
            return Token(access_token=access_token, hasClient=has_client,
                role=user.role, id=user.id)

        except HTTPException:
            raise
        except Exception as e:
            print(f"❌ Error al registrar usuario: {e}")
            raise internal_server_error("No se pudo registrar el usuario.")

    @staticmethod
    def login(credentials: UserLogin, db: Session):
        try:
            user = UserRepository.find_by_email(db, credentials.email)
            if not user or not pwd_context.verify(credentials.password, user.hashed_password):
                raise invalid_credentials()

            access_token = create_access_token(data={"sub": user.email})
            has_client = bool(user.cliente)
            cliente_id = user.cliente.id if user.cliente else None
            return Token(access_token=access_token, hasClient=has_client,
                role=user.role, id=cliente_id)

        except HTTPException:
            raise
        except Exception as e:
            print(f"❌ Error en login: {e}")
            raise internal_server_error("Error interno al iniciar sesión.")