import models.roles
import schemas.roles
from sqlalchemy.orm import Session

def get_rol(db:Session, id:int):
    return db.query(models.roles.Rol).filter(models.roles.Rol.id == id).first()

def get_rol_by_nombre(db: Session, nombre: str):
    return db.query(models.roles.Rol).filter(models.roles.Rol == nombre).first()

def get_rol(db: Session, skip:int=0,limit:int=10):
    return db.query(models.roles.Rol).offset(skip).limit(limit).all()

def create_rol(db: Session, rol:schemas.roles.RolCreate):
    db_rol = models.roles.Rol(nombre=rol.nombre, descripcion=rol.descripcion,created_at=rol.created_at, estatus=rol.estatus)
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol

def update_rol(db: Session, id: int, rol: schemas.roles.RolUpdate):
    db_rol = db.query(models.roles.Rol).filter(models.roles.Rol.id == id).first()
    if db_rol:
        for var, value in vars(rol).items():
            setattr(db_rol, var, value) if value else None
        db.commit()
        db.refresh(db_rol)
    return db_rol

def delete_rol(db: Session, id: int):
    db_rol = db.query(models.roles.Rol).filter(models.roles.Rol.id == id).first()
    if  db_rol:
        db.delete(db_rol)
        db.commit()
    return db_rol

