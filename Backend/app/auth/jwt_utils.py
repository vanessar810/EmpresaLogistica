from datetime import datetime, timedelta, timezone
from jose import jwt
from app.configuration.settings import settings

def create_access_token(data: dict, expires_delta: int = None):
    to_encode= data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_delta or settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except Exception:
        return None