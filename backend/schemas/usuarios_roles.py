from typing import List,Union
from pydantic import BaseModel
from datetime import datetime

class UsuarioRolBase(BaseModel):
    usuario_id:int
    rol_id:int
    created_at:datetime
    estatus:bool
    fecha_actualizacion:datetime
    
class UsuarioRolCreate(UsuarioRolBase):
    pass
class UsuarioRolUpdate(UsuarioRolBase):
    pass
class UsuarioRol(UsuarioRolBase):
    id:int
    #owner_id:int clave foranea
    
    class Config:
        orm_mode=True
        