from sqlalchemy import Column, Integer, String
from app.configuration.database import Base

class Bodega(Base):
    __tablename__ = "bodegas"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    ubicacion = Column(String(50), nullable=False)
