from pydantic import BaseModel
from datetime import date
class EnvioPrepararReq(BaseModel):
    productoId: int
    cantidad: int
    fechaRecogida: date
    bodegaId: int | None = None
    puertoId: int | None = None
    cliente_id: int