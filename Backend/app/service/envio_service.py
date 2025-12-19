from sqlalchemy.orm import Session
from app.entity.envio_terrestre import EnvioTerrestre
from app.entity.envio_maritimo import EnvioMaritimo
from app.repository.envio_repository import EnvioRepository
from app.utils.validators import validar_placa, validar_numero_flota
from app.exception.http_exceptions import  invalid_data_error, internal_server_error, envio_terrestre_not_found, envio_maritimo_not_found, draft_not_found
from app.dto.envio_dto import EnvioConfirmarReq
from app.entity.envio_preparado import EnvioPreparado
from app.service.producto_serive import ProductService
from app.service.bodega_service import BodegaService
from app.service.puerto_service import PuertoService

class EnvioService:
    @staticmethod
    def crear_envio_terrestre(db: Session, data: dict):
        try:
            validar_placa(data["placa"])
            envio = EnvioTerrestre(
            tipo_producto = ProductService.get_producto(db, data["producto_id"]).nombre,
            cantidad = data["cantidad"],
            fecha_registro = data["fecha_registro"],
            fecha_entrega = data["fecha_entrega"],
            bodega_entrega = BodegaService.get_bodega(db, data["bodega_id"]).nombre,
            precio_envio = data["precio_envio"],
            descuento = data["descuento"],
            placa = data["placa"],
            numero_guia = data["numero_guia"],
            cliente_id = data["cliente_id"],
        )
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
            envio = EnvioMaritimo(
            tipo_producto = ProductService.get_producto(db, data["producto_id"]).nombre,
            cantidad = data["cantidad"],
            fecha_registro = data["fecha_registro"],
            fecha_entrega = data["fecha_entrega"],
            puerto_entrega = PuertoService.get_puerto(db, data["puerto_id"]).nombre,
            precio_envio = data["precio_envio"],
            descuento = data["descuento"],
            numero_flota = data["numero_flota"],
            numero_guia = data["numero_guia"],
            cliente_id = data["cliente_id"],
        )

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
    

    
    @staticmethod
    def confirmar_envio(req: EnvioConfirmarReq, db: Session):
        draft = db.query(EnvioPreparado).filter_by(id=req.id).first()
        if not draft:
            raise draft_not_found
        data = EnvioService.draft_to_data(draft)
        if draft.puerto_id:
            envio = EnvioService.crear_envio_maritimo(db, data)
        else:
            envio = EnvioService.crear_envio_terrestre(db, data)

        # Eliminar draft y guardar cambios
        db.delete(draft)
        db.commit()

        return envio

    @staticmethod
    def draft_to_data(draft: "EnvioPreparado") -> dict:
        return {
            "producto_id": draft.producto_id,
            "cantidad": draft.cantidad,
            "fecha_registro": draft.fecha_registro,
            "fecha_entrega": draft.fecha_entrega,
            "bodega_id": draft.bodega_id,
            "puerto_id": draft.puerto_id,
            "precio_envio": draft.precio_envio,
            "descuento": draft.descuento,
            "placa": draft.placa,
            "numero_flota": draft.numero_flota,
            "numero_guia": draft.numero_guia,
            "cliente_id": draft.cliente_id,
        }
    
    @staticmethod
    def get_envios_by_cliente(db: Session, cliente_id: int):
        envios_terrestres = (
            db.query(EnvioTerrestre).filter(EnvioTerrestre.cliente_id == cliente_id).all()
        )
        envios_maritimos =(
            db.query(EnvioMaritimo).filter(EnvioMaritimo.cliente_id == cliente_id).all()
        )
        
        return {
            "terrestres": envios_terrestres,
            "maritimos": envios_maritimos
        }
