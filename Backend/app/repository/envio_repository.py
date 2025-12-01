from sqlalchemy.orm import Session

class EnvioRepository:
    @staticmethod
    def create(db: Session, envio):
        db.add(envio)
        db.commit()
        db.refresh(envio)
        return envio

    @staticmethod
    def get_by_id(db: Session, model, envio_id: int):
        return db.query(model).filter(model.id == envio_id).first()

    @staticmethod
    def get_all(db: Session, model, skip: int = 0, limit: int = 100, tipo_producto: str = None, cliente_id: int = None):
        query = db.query(model)
        if tipo_producto:
            query = query.filter(model.tipo_producto.ilike(f"%{tipo_producto}%"))
        if cliente_id:
            query = query.filter(model.cliente_id == cliente_id)
        return query.offset(skip).limit(limit).all()

    @staticmethod
    def delete(db: Session, envio):
        db.delete(envio)
        db.commit()

    @staticmethod
    def update(db: Session, envio):
        db.commit()
        db.refresh(envio)
        return envio