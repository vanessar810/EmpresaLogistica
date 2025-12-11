from sqlalchemy.orm import Session
from app.repository.cliente_repository import ClienteRepository
from app.entity.cliente import Cliente
from app.exception.http_exceptions import cliente_not_found, internal_server_error, user_already_exists
from fastapi import HTTPException
from app.entity.user import User

class ClienteService:
    @staticmethod
    def create_cliente(db: Session, user_id: int, nombre: str, telefono: str):
        try:
            existing = db.query(Cliente).filter_by(user_id=user_id).first()
            if existing:
                raise user_already_exists

            user = db.query(User).filter_by(id=user_id).first()
            if not user:
                    raise cliente_not_found
    
            cliente = Cliente(nombre=nombre, telefono=telefono, user_id=user_id, email=user.email)
            return ClienteRepository.create(db, cliente)

        except HTTPException as e:
            raise e
        except Exception as e:
            print(f"Error al crear cliente: {e}")
            raise internal_server_error("No se pudo crear el cliente.")

    @staticmethod
    def get_cliente(db: Session, cliente_id: int):
        try:
            cliente = ClienteRepository.get_by_id(db, cliente_id)
            if not cliente:
                raise cliente_not_found()
            return cliente
        except Exception as e:
            print(f"Error al obtener cliente: {e}")
            raise internal_server_error("Error interno al consultar cliente.")

    @staticmethod
    def get_clientes(db: Session, skip: int = 0, limit: int = 100, nombre: str = None):
        return ClienteRepository.get_all(db, skip, limit, nombre)

    @staticmethod
    def update_cliente(db: Session, cliente_id: int, data: dict):
        cliente = ClienteService.get_cliente(db, cliente_id)
        for key, value in data.items():
            if value is not None:
                setattr(cliente, key, value)
        return ClienteRepository.update(db, cliente)

    @staticmethod
    def delete_cliente(db: Session, cliente_id: int):
        cliente = ClienteService.get_cliente(db, cliente_id)
        ClienteRepository.delete(db, cliente)