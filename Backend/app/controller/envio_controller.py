from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.configuration.database import get_db
from app.dto.envio_dto import EnvioTerrestreDTO, EnvioMaritimoDTO
from app.service.envio_service import EnvioService

router = APIRouter(prefix="/envios", tags=["envios"])

# --- Envíos terrestres ---
@router.post("/terrestres")
def create_envio_terrestre(envio: EnvioTerrestreDTO, db: Session = Depends(get_db)):
    return EnvioService.crear_envio_terrestre(db, envio.dict())

@router.get("/terrestres/{envio_id}")
def get_envio_terrestre(envio_id: int, db: Session = Depends(get_db)):
    return EnvioService.get_envio_terrestre(db, envio_id)

@router.get("/terrestres")
def list_envios_terrestres(skip: int = 0, limit: int = 100, tipo_producto: str = None, cliente_id: int = None, db: Session = Depends(get_db)):
    return EnvioService.list_envios_terrestres(db, skip, limit, tipo_producto, cliente_id)

@router.put("/terrestres/{envio_id}")
def update_envio_terrestre(envio_id: int, data: EnvioTerrestreDTO, db: Session = Depends(get_db)):
    return EnvioService.update_envio_terrestre(db, envio_id, data.dict())

@router.delete("/terrestres/{envio_id}")
def delete_envio_terrestre(envio_id: int, db: Session = Depends(get_db)):
    envio = EnvioService.get_envio_terrestre(db, envio_id)
    EnvioService.delete_envio(db, envio)
    return {"detail": "Envio terrestre eliminado"}

# --- Envíos marítimos ---
@router.post("/maritimos")
def create_envio_maritimo(envio: EnvioMaritimoDTO, db: Session = Depends(get_db)):
    return EnvioService.crear_envio_maritimo(db, envio.dict())

@router.get("/maritimos/{envio_id}")
def get_envio_maritimo(envio_id: int, db: Session = Depends(get_db)):
    return EnvioService.get_envio_maritimo(db, envio_id)

@router.get("/maritimos")
def list_envios_maritimos(skip: int = 0, limit: int = 100, tipo_producto: str = None, cliente_id: int = None, db: Session = Depends(get_db)):
    return EnvioService.list_envios_maritimos(db, skip, limit, tipo_producto, cliente_id)

@router.put("/maritimos/{envio_id}")
def update_envio_maritimo(envio_id: int, data: EnvioMaritimoDTO, db: Session = Depends(get_db)):
    return EnvioService.update_envio_maritimo(db, envio_id, data.dict())

@router.delete("/maritimos/{envio_id}")
def delete_envio_maritimo(envio_id: int, db: Session = Depends(get_db)):
    envio = EnvioService.get_envio_maritimo(db, envio_id)
    EnvioService.delete_envio(db, envio)
    return {"detail": "Envio marítimo eliminado"}