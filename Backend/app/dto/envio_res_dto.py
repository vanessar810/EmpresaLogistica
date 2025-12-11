from pydantic import BaseModel
from datetime import date
class EnvioPrepararRes(BaseModel):
    id: int 
    precioEnvio: float
    precioProductos: float
    descuento : float
    total: float
    numeroGuia: str
    numeroFlota: str | None = None
    placa: str | None = None
    fechaEntrega: date