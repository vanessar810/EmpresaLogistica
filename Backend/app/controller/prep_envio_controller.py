from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.configuration.database import get_db
from app.dto.envio_res_dto import EnvioPrepararRes
from app.dto.envio_req_dto import EnvioPrepararReq
from app.service.prepara_envio_service import PreparacionEnvioService

router = APIRouter(prefix="/preparacion", tags=["Preparación Envios"])

@router.post("/envio", response_model=EnvioPrepararRes)
def preparar_envio(req: EnvioPrepararReq, db: Session = Depends(get_db)):
    return PreparacionEnvioService.calcular_precio_envio(db, req)