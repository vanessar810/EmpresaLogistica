from pydantic import BaseModel, Field
from datetime import date


class EnvioTerrestreDTO(BaseModel):
    id: int
    tipo_producto: str
    cantidad: int = Field(..., gt=0)
    fecha_registro: date
    fecha_entrega: date
    bodega_entrega: str
    precio_envio: float = Field(..., gt=0)
    placa: str
    numero_guia: str
    cliente_id: int
    precio_envio: int
    descuento: float
    total: float

    model_config = {
        "from_attributes": True
    }


class EnvioMaritimoDTO(BaseModel):
    id: int
    tipo_producto: str
    cantidad: int = Field(..., gt=0)
    fecha_registro: date
    fecha_entrega: date
    puerto_entrega: str
    precio_envio: float = Field(..., gt=0)
    numero_flota: str
    numero_guia: str
    cliente_id: int
    precio_envio: int
    descuento: float
    total: float

    model_config = {
        "from_attributes": True
    }

class EnvioConfirmarReq(BaseModel):
    id: int