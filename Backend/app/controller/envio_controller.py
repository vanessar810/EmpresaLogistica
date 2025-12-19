from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.configuration.database import get_db
from app.dto.envio_dto import EnvioTerrestreDTO, EnvioMaritimoDTO, EnvioConfirmarReq
from app.service.envio_service import EnvioService
from app.auth.security import get_current_user
from app.entity.user import User
from app.entity.cliente import Cliente
from app.service.cliente_service import ClienteService

router = APIRouter(prefix="/envios", tags=["envios"])

# --- Envíos terrestres ---
@router.post("/terrestres")
def create_envio_terrestre(envio: EnvioTerrestreDTO, db: Session = Depends(get_db)):
    return EnvioService.crear_envio_terrestre(db, envio())

@router.get("/terrestres/{envio_id}")
def get_envio_terrestre(envio_id: int, db: Session = Depends(get_db)):
    return EnvioService.get_envio_terrestre(db, envio_id)

@router.get("/terrestres")
def list_envios_terrestres(skip: int = 0, limit: int = 100, tipo_producto: str = None, cliente_id: int = None, db: Session = Depends(get_db)):
    return EnvioService.list_envios_terrestres(db, skip, limit, tipo_producto, cliente_id)

@router.put("/terrestres/{envio_id}")
def update_envio_terrestre(envio_id: int, data: EnvioTerrestreDTO, db: Session = Depends(get_db)):
    return EnvioService.update_envio_terrestre(db, envio_id, data())

@router.delete("/terrestres/{envio_id}")
def delete_envio_terrestre(envio_id: int, db: Session = Depends(get_db)):
    envio = EnvioService.get_envio_terrestre(db, envio_id)
    EnvioService.delete_envio(db, envio)
    return {"detail": "Envio terrestre eliminado"}

# --- Envíos marítimos ---
@router.post("/maritimos")
def create_envio_maritimo(envio: EnvioMaritimoDTO, db: Session = Depends(get_db)):
    return EnvioService.crear_envio_maritimo(db, envio())

@router.get("/maritimos/{envio_id}")
def get_envio_maritimo(envio_id: int, db: Session = Depends(get_db)):
    return EnvioService.get_envio_maritimo(db, envio_id)

@router.get("/maritimos")
def list_envios_maritimos(skip: int = 0, limit: int = 100, tipo_producto: str = None, cliente_id: int = None, db: Session = Depends(get_db)):
    return EnvioService.list_envios_maritimos(db, skip, limit, tipo_producto, cliente_id)

@router.put("/maritimos/{envio_id}")
def update_envio_maritimo(envio_id: int, data: EnvioMaritimoDTO, db: Session = Depends(get_db)):
    return EnvioService.update_envio_maritimo(db, envio_id, data())

@router.delete("/maritimos/{envio_id}")
def delete_envio_maritimo(envio_id: int, db: Session = Depends(get_db)):
    envio = EnvioService.get_envio_maritimo(db, envio_id)
    EnvioService.delete_envio(db, envio)
    return {"detail": "Envio marítimo eliminado"}

@router.post("/confirmar")
def confirmar(req: EnvioConfirmarReq, db: Session = Depends(get_db)):
    return EnvioService.confirmar_envio(req, db)

@router.get("/mis-envios")
def get_envios(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    Cliente = ClienteService.get_cliente_by_user_id(db, current_user.id)
    if not Cliente:
        raise HTTPException(
            status_code=404,
            detail="El usuario no tiene perfil de cliente"
        )
    return EnvioService.get_envios_by_cliente(db, Cliente.id)
    