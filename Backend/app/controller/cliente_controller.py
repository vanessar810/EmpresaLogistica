from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.configuration.database import get_db
from app.dto.cliente_dto import ClienteCreateDTO, ClienteUpdateDTO, ClienteDTO
from app.service.cliente_service import ClienteService
from app.auth.security import get_current_user
from app.entity.user import User
from app.dto.cliente_dto import ClienteDTO

router = APIRouter(prefix="/clientes", tags=["clientes"])

@router.post("/", response_model=ClienteDTO)
def create_cliente(cliente: ClienteCreateDTO, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    nuevo_cliente = ClienteService.create_cliente(
        db,
        current_user.id,
        cliente.nombre,
        cliente.telefono)
    db.refresh(nuevo_cliente)
    return ClienteDTO(id=nuevo_cliente.id, nombre=nuevo_cliente.nombre, telefono=nuevo_cliente.telefono, email =nuevo_cliente.email)

@router.get("/{cliente_id}",dependencies=[Depends(get_current_user)], response_model=ClienteDTO)
def get_cliente(cliente_id: int, db: Session = Depends(get_db)):
    return ClienteService.get_cliente(db, cliente_id)

@router.get("/",dependencies=[Depends(get_current_user)], response_model=list[ClienteDTO])
def list_clientes(skip: int = 0, limit: int = 100, nombre: str = None, db: Session = Depends(get_db)):
    return ClienteService.get_clientes(db, skip, limit, nombre)

@router.put("/{cliente_id}", response_model=ClienteDTO)
def update_cliente(cliente_id: int, data: ClienteUpdateDTO, db: Session = Depends(get_db)):
    return ClienteService.update_cliente(db, cliente_id, data.dict())

@router.delete("/{cliente_id}", dependencies=[Depends(get_current_user)],)
def delete_cliente(cliente_id: int, db: Session = Depends(get_db)):
    ClienteService.delete_cliente(db, cliente_id)
    return {"detail": "Cliente eliminado"}