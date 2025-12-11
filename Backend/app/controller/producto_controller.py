from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.configuration.database import get_db
from app.service.producto_serive import ProductService

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.get("/")
def get_productos(db: Session = Depends(get_db)):
    return ProductService.get_all_productos(db)

@router.get("/{producto_id}")
def get_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = ProductService.get_producto(db, producto_id)
    if not producto:
        return {"error": "Producto no encontrado"}
    return producto