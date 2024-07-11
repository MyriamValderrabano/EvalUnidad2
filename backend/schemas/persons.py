from typing import List,Union
from pydantic import BaseModel
from datetime import datetime

class PersonBase(BaseModel):
    titulo_cortesia:str
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    curp: str
    genero: str
    sangre: str
    fecha_nacimiento: datetime
    fotografia:str
    telefono: str
    correo_electronico: str
    created_at:datetime
    estatus:bool
    
    
class PersonCreate(PersonBase):
    pass
class PersonUpdate(PersonBase):
    pass
class Person(PersonBase):
    id:int
    #owner_id:int clave foranea
    
    class Config:
        orm_mode=True
        