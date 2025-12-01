from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from app.configuration.database import Base

class EnvioMaritimo(Base):
    __tablename__ = "envios_maritimos"
    id = Column(Integer, primary_key=True, index=True)
    tipo_producto = Column(String(100))
    cantidad = Column(Integer)
    fecha_registro = Column(Date)
    fecha_entrega = Column(Date)
    puerto_entrega = Column(String(100))
    precio_envio = Column(Float)
    descuento = Column(Float)
    numero_flota = Column(String(8), unique=True)
    numero_guia = Column(String(10), unique=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))