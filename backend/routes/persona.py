from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

persona= APIRouter()
personas=[]
class model_personas(BaseModel):
    id:int
    nombre:str
    primer_apellido: str
    segundo_apellido:Optional[str] 
    edad:int
    fecha_nacimiento:datetime
    curp:str
    tipo_sangre:str
    created_at:datetime = datetime.now()
    estatus: bool = False



@persona.get('/')
def bienvenida():
    return "Bienvenido al api del sistema"

@persona.get("/personas")
def get_personas():
    return personas

@persona.post("/personas")
def savePersonas(datos_persona:model_personas):
    personas.append(datos_persona)
    return "Datos guardados correctamente"


@persona.put("/personas/{persona_id}")
def updatePersonas(persona_id: int, datos_persona: model_personas):
    for index, persona in enumerate(personas):
        if persona.id == persona_id:
            datos_persona.id=persona.id
            personas[index] = datos_persona
            return "Datos actualizados correctamente"

@persona.delete("/personas/{persona_id}")
def deletePersonas(persona_id: int):
    for index, persona in enumerate(personas):
        if persona.id == persona_id:
            del personas[index]
            return "Datos eliminados correctamente"

@persona.get("/personas/{persona_id}")
def get_Personas(persona_id: int):
    for persona in personas:
        if persona.id == persona_id:
            return persona
