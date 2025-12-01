from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.configuration.settings import settings
from app.exception.http_exceptions import invalid_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Verifica que el token JWT sea válido.
    Si no lo es, lanza un error 401.
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise invalid_token()
    except JWTError:
        raise invalid_token()

    return payload  # contiene datos del usuario