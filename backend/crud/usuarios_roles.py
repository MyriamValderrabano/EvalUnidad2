import models.usuarios_roles
import schemas.usuarios_roles
from sqlalchemy.orm import Session

def get_UserRol(db:Session, id:int):
    return db.query(models.usuarios_roles.Usuario_Rol).filter(models.usuarios_roles.Usuario_Rol.usuario_id == id).first()


def get_UserRol(db: Session, skip:int=0,limit:int=10):
    return db.query(models.usuarios_roles.Usuario_Rol).offset(skip).limit(limit).all()

def get_userrol_by_userrol(db: Session, usuario_id: int):
    return db.query(models.usuarios_roles.Usuario_Rol).filter(models.usuarios_roles.Usuario_Rol == usuario_id).first()

def create_UserRol(db: Session, usuario_rol:schemas.usuarios_roles.UsuarioRolCreate):
    db_UserRol = models.usuarios_roles.Usuario_Rol(usuario_id=usuario_rol.usuario_id,rol_id=usuario_rol.rol_id, estatus=usuario_rol.estatus,created_at=usuario_rol.created_at, fecha_actualizacion=usuario_rol.fecha_actualizacion)
    db.add(db_UserRol)
    db.commit()
    db.refresh(db_UserRol)
    return db_UserRol

def update_UserRol(db: Session, id: int, roles: schemas.usuarios_roles.UsuarioRolUpdate):
    db_UserRol = db.query(models.usuarios_roles.Usuario_Rol).filter(models.usuarios_roles.Usuario_Rol.usuario_id == id).first()
    if db_UserRol:
        for var, value in vars(roles).items():
            setattr(db_UserRol, var, value) if value else None
        db.commit()
        db.refresh(db_UserRol)
    return db_UserRol

def delete_UserRol(db: Session, id: int):
    db_UserRol = db.query(models.usuarios_roles.Usuario_Rol).filter(models.usuarios_roles.Usuario_Rol.usuario_id == id).first()
    if  db_UserRol:
        db.delete(db_UserRol)
        db.commit()
    return db_UserRol

