from fastapi import APIRouter,HTTPException,Depends,Request
from sqlalchemy.orm import Session
import crud.usuarios_roles,config.db,schemas.usuarios_roles,models.usuarios_roles
from typing import List

userRol = APIRouter()

models.roles.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@userRol.get("/usuarios_roles/", response_model=List[schemas.usuarios_roles.UsuarioRol], tags=["usuarios_roles"])
def read_usuarios_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_UserRols= crud.usuarios_roles.get_usuarios_roles(db=db, skip=skip, limit=limit)
    return db_UserRols

@userRol.post("/usuarios_roles/{id}", response_model=schemas.usuarios_roles.UsuarioRol, tags=["usuarios_roles"])
def read_usuarios_roles(id: int, db: Session = Depends(get_db)):
    db_UserRol= crud.usuarios_roles.get_rol(db=db, id=id)
    if db_UserRol is None:
        raise HTTPException(status_code=404, detail="usuarios_roles not found")
    return db_UserRol

@userRol.post("/usuarios_roles/", response_model=schemas.usuarios_roles.UsuarioRol, tags=["usuarios_roles"])
def create_usuarios_roles(rol: schemas.usuarios_roles.UsuarioRolCreate, db: Session = Depends(get_db)):
    db_UserRol = crud.usuarios_roles.get_rol_by_usuario(db, usuario_id=userRol.usuario_id)
    if db_UserRol:
        raise HTTPException(status_code=400, detail="Rol existente intenta nuevamente")
    return crud.usuarios_roles.create_usuarios_roles(db=db, rol=rol)

@userRol.put("/usuarios_roles/{id}", response_model=schemas.usuarios_roles.UsuarioRol, tags=["usuarios_roles"])
def update_usuarios_roles(id: int, rol: schemas.usuarios_roles.UsuarioRolUpdate, db: Session = Depends(get_db)):
    db_UserRol = crud.usuarios_roles.update_rol(db = db, id = id, rol = rol)
    if db_UserRol is None:
        raise HTTPException(status_code=404, detail="usuarios_roles no existente, no esta actuaizado")
    return db_UserRol

@userRol.delete("/usuarios_roles/{id}", response_model=schemas.usuarios_roles.UsuarioRol, tags=["usuarios_roles"])
def delete_rol(id: int, db: Session = Depends(get_db)):
    db_UserRol = crud.usuarios_roles.delete_usuarios_roles(db = db, id = id)
    if db_UserRol is None:
        raise HTTPException(status_code=404, detail="Rol no existe, no se pudo eliminar")
    return db_UserRol