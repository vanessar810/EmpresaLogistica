from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.configuration.database import get_db
from app.service.bodega_service import BodegaService

router = APIRouter(prefix="/bodega", tags=["Bodega"])

@router.get("/")
def get_bodegas(db: Session= Depends(get_db)):
    return BodegaService.get_all_bodegas(db)

@router.get("/{bodega_id}")
def get_bodega(bodega_id: int, db: Session = Depends(get_db)):
    bodega = BodegaService.get_bodega(db, bodega_id)
    if not bodega:
        return{"error: bodega no encontrada"}
    return bodega