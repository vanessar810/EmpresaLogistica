import random, string
from sqlalchemy.orm import Session
from app.utils.generators import generar_numero_guia, generar_flota, generar_placa
from app.dto.envio_req_dto import EnvioPrepararReq
from app.dto.envio_res_dto import EnvioPrepararRes
from app.service.producto_serive import ProductService
from app.entity.envio_preparado import EnvioPreparado
from datetime import timedelta


class PreparacionEnvioService:

    @staticmethod
    def calcular_precio_envio(db: Session, req: EnvioPrepararReq):
        try:
            if req.bodegaId is not None:
                origen = "terrestre"
            elif req.puertoId is not None:
                origen = "maritimo"
            else:
                raise ValueError("Debe enviar bodegaId o puertoId")
            producto = ProductService.get_producto(db, req.productoId)
            precio_producto = producto.precio
            descuento = 0
            placa = None
            flota = None

            if origen == "terrestre":
                precio_envio = 100
                fecha_entrega = req.fechaRecogida + timedelta(days=3)
                placa = generar_placa()
                if req.cantidad > 10:
                    descuento = precio_producto * 0.05 * req.cantidad
            if origen == "maritimo":
                precio_envio = 300
                fecha_entrega = req.fechaRecogida + timedelta(days=10)
                flota = generar_flota()
                if req.cantidad > 10:
                    descuento = precio_producto * 0.03 * req.cantidad

            total = precio_envio + precio_producto * req.cantidad - descuento
            guia = generar_numero_guia()

            #Crea borrador y lo guarda en DB
            draft = EnvioPreparado(
                producto_id=req.productoId,
                cantidad=req.cantidad,
                fecha_recogida=req.fechaRecogida,
                puerto_id=req.puertoId,
                bodega_id=req.bodegaId,
                precio_envio=precio_envio,
                precio_productos=precio_producto,
                descuento=descuento,
                cliente_id = req.cliente_id,
                total=total,
                numero_guia=guia,
                numero_flota=flota,
                placa=placa,
                fecha_entrega=fecha_entrega
        
            )
            db.add(draft)
            db.commit()
            db.refresh(draft)

            return EnvioPrepararRes(
                id=draft.id,
                producto = producto.nombre,
                cantidad = draft.cantidad,
                precioEnvio=precio_envio,
                precioProductos=precio_producto,
                descuento=descuento,
                total=total,
                numeroGuia=guia,
                numeroFlota=flota,
                placa=placa,
                fechaEntrega=fecha_entrega,
            )
        except Exception as e:
            print(f"error calculando precio: {e}")
            return None
