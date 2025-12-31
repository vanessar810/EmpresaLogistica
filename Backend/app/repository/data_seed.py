from sqlalchemy.orm import Session
from app.entity.producto import Producto
from app.entity.puerto import Puerto
from app.entity.bodega import Bodega
from app.configuration.settings import settings
print("DB URL:", settings.DATABASE_URL)

def seed_data(db: Session):
    print("Iniciando seed...")
    if db.query(Producto).first():
        return
    productos = [
        Producto(nombre= "Electrónicos", precio=125 ),
        Producto(nombre= "Autos", precio= 500),
        Producto(nombre= "Textiles", precio=100),
        Producto(nombre= "Alimentos", precio=50)
    ]
    
    bodegas = [
        Bodega(nombre= "Bodega Central Bogotá", ubicacion= "Bogotá"),
        Bodega(nombre= "Bodega Norte Medellín", ubicacion= "Medellín"),
        Bodega(nombre= "Bodega Central Cali", ubicacion= "Cali"),
        Bodega(nombre= "Bodega Central Barranquilla", ubicacion= "Barranquilla")
    ]
    
    puertos = [
        Puerto(nombre= "Puerto de Cartagena", ubicacion= "Colombia"),
        Puerto(nombre= "Puerto de Buenaventura", ubicacion= "Colombia")
    ]
    print("Seed completado.")
    db.add_all(productos)
    db.add_all(bodegas)
    db.add_all(puertos)
    db.commit()
    