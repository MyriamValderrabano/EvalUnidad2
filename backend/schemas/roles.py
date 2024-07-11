from typing import List,Union
from pydantic import BaseModel
from datetime import datetime

class RolBase(BaseModel):
    nombre: str
    descripcion: str
    created_at:datetime
    estatus:bool
    
    
class RolCreate(RolBase):
    pass
class RolUpdate(RolBase):
    pass
class Rol(RolBase):
    id:int
    #owner_id:int clave foranea
    
    class Config:
        orm_mode=True
        