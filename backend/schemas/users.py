from typing import List, Optional, Union
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

class UserLogin(BaseModel):
    Nombre_Usuario: Optional[str]=None
    Correo_Electronico: Optional[str]=None
    Contrasena: str
    Numero_Telefonico_Movil: Optional[str]=None