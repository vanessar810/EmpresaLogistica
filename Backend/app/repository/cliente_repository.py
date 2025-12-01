from sqlalchemy.orm import Session
from app.entity.cliente import Cliente

class ClienteRepository:
    @staticmethod
    def create(db: Session, cliente: Cliente):
        db.add(cliente)
        db.commit()
        db.refresh(cliente)
        return cliente

    @staticmethod
    def get_by_id(db: Session, cliente_id: int):
        return db.query(Cliente).filter(Cliente.id == cliente_id).first()

    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100, nombre: str = None):
        query = db.query(Cliente)
        if nombre:
            query = query.filter(Cliente.nombre.ilike(f"%{nombre}%"))
        return query.offset(skip).limit(limit).all()

    @staticmethod
    def update(db: Session, cliente: Cliente):
        db.commit()
        db.refresh(cliente)
        return cliente

    @staticmethod
    def delete(db: Session, cliente: Cliente):
        db.delete(cliente)
        db.commit()