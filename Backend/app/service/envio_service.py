from sqlalchemy.orm import Session
from app.entity.envio_terrestre import EnvioTerrestre
from app.entity.envio_maritimo import EnvioMaritimo
from app.repository.envio_repository import EnvioRepository
from app.utils.validators import validar_placa, validar_numero_flota
from app.exception.http_exceptions import  invalid_data_error, internal_server_error, envio_terrestre_not_found, envio_maritimo_not_found

class EnvioService:
    @staticmethod
    def crear_envio_terrestre(db: Session, data: dict):
        try:
            validar_placa(data["placa"])
            descuento = 0
            if data["cantidad"] > 10:
                descuento = data["precio_envio"] * 0.05
            envio = EnvioTerrestre(**data, descuento=descuento)
            return EnvioRepository.create(db, envio)

        except KeyError as e:
            raise invalid_data_error(f"Campo faltante: {e}")
        except Exception as e:
            print(f"Error al crear envío terrestre: {e}")
            raise internal_server_error("No se pudo crear el envío terrestre.")

    @staticmethod
    def crear_envio_maritimo(db: Session, data: dict):
        try:
            validar_numero_flota(data["numero_flota"])
            descuento = 0
            if data["cantidad"] > 10:
                descuento = data["precio_envio"] * 0.03

            envio = EnvioMaritimo(**data, descuento=descuento)
            return EnvioRepository.create(db, envio)
    
        except KeyError as e:
            raise invalid_data_error(f"Campo faltante: {e}")
        except Exception as e:
            print(f"Error al crear envío marítimo: {e}")
            raise internal_server_error("No se pudo crear el envío marítimo.")

    @staticmethod
    def get_envio_terrestre(db: Session, envio_id: int):
        envio = EnvioRepository.get_by_id(db, EnvioTerrestre, envio_id)
        if not envio:
            raise envio_terrestre_not_found
        return envio

    @staticmethod
    def get_envio_maritimo(db: Session, envio_id: int):
        envio = EnvioRepository.get_by_id(db, EnvioMaritimo, envio_id)
        if not envio:
            raise envio_maritimo_not_found
        return envio

    @staticmethod
    def list_envios_terrestres(db: Session, skip: int = 0, limit: int = 100, tipo_producto: str = None, cliente_id: int = None):
        return EnvioRepository.get_all(db, EnvioTerrestre, skip, limit, tipo_producto, cliente_id)

    @staticmethod
    def list_envios_maritimos(db: Session, skip: int = 0, limit: int = 100, tipo_producto: str = None, cliente_id: int = None):
        return EnvioRepository.get_all(db, EnvioMaritimo, skip, limit, tipo_producto, cliente_id)

    @staticmethod
    def delete_envio(db: Session, envio):
        EnvioRepository.delete(db, envio)

    @staticmethod
    def update_envio_terrestre(db: Session, envio_id: int, data: dict):
        envio = EnvioService.get_envio_terrestre(db, envio_id)
        for key, value in data.items():
            if value is not None:
                setattr(envio, key, value)
        return EnvioRepository.update(db, envio)

    @staticmethod
    def update_envio_maritimo(db: Session, envio_id: int, data: dict):
        envio = EnvioService.get_envio_maritimo(db, envio_id)
        for key, value in data.items():
            if value is not None:
                setattr(envio, key, value)
        return EnvioRepository.update(db, envio)