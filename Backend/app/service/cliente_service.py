from sqlalchemy.orm import Session
from app.repository.cliente_repository import ClienteRepository
from app.entity.cliente import Cliente
from app.exception.http_exceptions import invalid_data_error, internal_server_error
from fastapi import HTTPException

class ClienteService:
    @staticmethod
    def create_cliente(db: Session, nombre: str, email: str, telefono: str | None):
        try:
            if not nombre or not email:
                raise invalid_data_error("El nombre y el correo son obligatorios.")
            
            cliente = Cliente(nombre=nombre, email=email, telefono=telefono)
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
                from app.exception.http_exceptions import cliente_not_found
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