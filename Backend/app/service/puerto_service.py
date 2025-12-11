from sqlalchemy.orm import Session
from app.entity.puerto import Puerto

class PuertoService:
    @staticmethod
    def get_puerto(db: Session, puerto_id:int):
        try:
            return db.query(Puerto).filter(Puerto.id == puerto_id).first()
        except Exception as e:
            print(f"error al obtener puerto: {e}")
            return None
        
    @staticmethod
    def get_all_puertos(db: Session):
            try:
                return db.query(Puerto).all()
            except Exception as e:
                print(f"Error al obtener lista de puerto:  {e}")
                return []