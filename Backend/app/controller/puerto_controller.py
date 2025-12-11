from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.configuration.database import get_db
from app.service.puerto_service import PuertoService

router = APIRouter(prefix="/puertos", tags=["Puertos"])

@router.get("/")
def get_puertos(db: Session = Depends(get_db)):
    return PuertoService.get_all_puertos(db)

@router.get("/{puerto_id}")
def get_puerto(puerto_id: int, db: Session = Depends(get_db)):
    puerto = PuertoService.get_puerto(db, puerto_id)
    if not puerto:
        return {"error: puerto no encontrado"}
    return puerto