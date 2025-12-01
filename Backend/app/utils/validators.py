import re
from fastapi import HTTPException, status

def validar_placa(placa: str):
    if not re.fullmatch(r"[A-Z]{3}[0-9]{3}", placa):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="Placa inválida. Formato: 3 letras + 3 números")

def validar_numero_flota(numero: str):
    if not re.fullmatch(r"[A-Z]{3}[0-9]{4}[A-Z]", numero):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="Número de flota inválido. Formato: AAA0000A")