from typing import List,Union
from pydantic import BaseModel
from datetime import datetime

class RolBase(BaseModel):
    Nombre: str
    Descripcion: str
    Created_at:datetime
    Estatus:bool
    
    
class RolCreate(RolBase):
    pass
class RolUpdate(RolBase):
    pass
class Rol(RolBase):
    ID:int
    #owner_id:int clave foranea
    
    class Config:
        orm_mode=True
        