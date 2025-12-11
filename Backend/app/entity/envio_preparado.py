from sqlalchemy import Column, Integer, String, Float, Date
from datetime import date
from app.configuration.database import Base

#sirve como borrador mientras el usuario visualiza y confirma el pedido, luego se borra. 
class EnvioPreparado(Base):
    __tablename__ = "envios_preparados"

    id = Column(Integer, primary_key= True, index = True)

    # datos originales de la solicitud
    producto_id = Column(Integer)
    cantidad = Column(Integer)
    fecha_recogida = Column(Date)
    puerto_id = Column(Integer, nullable=True)
    bodega_id = Column(Integer, nullable=True)
    cliente_id = Column(Integer)

    # datos calculados
    precio_envio = Column(Float)
    precio_productos = Column(Float)
    descuento = Column(Float)
    total = Column(Float)
    numero_guia = Column(String(10), unique=True)
    numero_flota = Column(String(8), nullable=True)
    placa = Column(String(8), nullable=True)
    fecha_entrega = Column(Date)

    fecha_registro = Column(Date, default=date.today())