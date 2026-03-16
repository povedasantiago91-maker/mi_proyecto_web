from sqlalchemy import Column, Integer, String
from database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    correo = Column(String(50))
    password = Column(String(100))
    is_admin = Column(Integer)