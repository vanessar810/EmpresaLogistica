from pydantic import BaseModel, Field
from datetime import date

class EnvioTerrestreDTO(BaseModel):
    tipo_producto: str
    cantidad: int = Field(..., gt=0)
    fecha_registro: date
    fecha_entrega: date
    bodega_entrega: str
    precio_envio: float = Field(..., gt=0)
    placa: str
    numero_guia: str
    cliente_id: int

class EnvioMaritimoDTO(BaseModel):
    tipo_producto: str
    cantidad: int = Field(..., gt=0)
    fecha_registro: date
    fecha_entrega: date
    puerto_entrega: str
    precio_envio: float = Field(..., gt=0)
    numero_flota: str
    numero_guia: str
    cliente_id: int

class EnvioConfirmarReq(BaseModel):
    id: int