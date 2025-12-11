from sqlalchemy.orm import Session
from app.entity.bodega import Bodega


class BodegaService:
    @staticmethod
    def get_bodega(db: Session, bodega_id: int):
        try:
            return db.query(Bodega).filter(Bodega.id == bodega_id).first()
        except Exception as e:
            print(f"error al obtener bodega: {e}")
            return None

    @staticmethod
    def get_all_bodegas(db: Session):
        try:
            return db.query(Bodega).all()
        except Exception as e:
            print(f"Error al obtener lista de bodegas: {e}")
            return []