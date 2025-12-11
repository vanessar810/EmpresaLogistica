from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.configuration.database import get_db
from sqlalchemy.orm import Session
from app.configuration.settings import settings
from app.exception.http_exceptions import invalid_token
from app.entity.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Verifica que el token JWT sea válido.
    Si no lo es, lanza un error 401.
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise invalid_token()
    except JWTError:
        raise invalid_token()

    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise invalid_token()

    return user