from sqlalchemy.orm import Session
from app.entity.producto import Producto

class ProductService:
    @staticmethod
    def get_producto(db: Session, producto_id:int):
        try:
            return db.query(Producto).filter(Producto.id == producto_id).first()
        except Exception as e:
            print(f"error al obtener producto: {e}")
            return None
        
    @staticmethod
    def get_all_productos(db: Session):
            try:
                return db.query(Producto).all()
            except Exception as e:
                print(f"Error al obtener lista de productos: {e}")
                return []