from pydantic import BaseModel, EmailStr

class ClienteCreateDTO(BaseModel):
    nombre: str
    email: EmailStr
    telefono: str | None

class ClienteUpdateDTO(BaseModel):
    nombre: str | None
    email: EmailStr | None
    telefono: str | None

class ClienteDTO(BaseModel):
    id: int
    nombre: str
    email: str
    telefono: str | None

    class Config:
        orm_mode = True