from sqlalchemy.orm import Session
import models


def crear_usuario(db: Session, nombre, correo, password, admin):

    user = models.Usuario(
        nombre=nombre,
        correo=correo,
        password=password,
        is_admin=admin
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user