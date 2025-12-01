from fastapi import HTTPException, status


#  Cliente no encontrado
def cliente_not_found():
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Cliente no encontrado."
    )


# Envío terrestre no encontrado
def envio_terrestre_not_found():
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Envío terrestre no encontrado."
    )


# Envío marítimo no encontrado
def envio_maritimo_not_found():
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Envío marítimo no encontrado."
    )


# Token inválido o expirado
def invalid_token():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido o expirado.",
        headers={"WWW-Authenticate": "Bearer"},
    )


# Datos inválidos o mal formateados
def invalid_data_error(message: str = "Datos inválidos o mal formateados."):
    return HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail=message
    )


# Error interno del servidor
def internal_server_error(message: str = "Error interno del servidor."):
    return HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=message
    )


# Usuario ya registrado
def user_already_exists():
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="El usuario ya se encuentra registrado."
    )


# Credenciales inválidas
def invalid_credentials():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales incorrectas. Verifica usuario o contraseña.",
        headers={"WWW-Authenticate": "Bearer"},
    )