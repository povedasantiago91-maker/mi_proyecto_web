from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
import schemas
import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/usuarios")
def crear_usuario(
    user: schemas.UsuarioCreate,
    db: Session = Depends(get_db)
):
    return crud.crear_usuario(
        db,
        user.nombre,
        user.correo,
        user.password,
        1
    )