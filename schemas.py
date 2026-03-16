from pydantic import BaseModel


class UsuarioCreate(BaseModel):
    nombre: str
    correo: str
    password: str


class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    correo: str
    is_admin: int

    class Config:
        from_attributes = True