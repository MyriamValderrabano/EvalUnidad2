from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

from models.users import MyEstatus

class UserBase(BaseModel):
    Persona_ID: int
    Nombre_Usuario: str
    Correo_Electronico: str
    Contrasena: str
    Numero_Telefonico_Movil: str
    Estatus: MyEstatus
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    ID: int
    Persona_ID: int
    class Config:
        orm_mode = True