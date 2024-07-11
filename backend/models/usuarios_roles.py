from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class Usuario_Rol(Base):
    __tablename__ = "usuarios_roles"
    
    id=Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, index=True)
    rol_id = Column(Integer ,index=True)
    created_at = Column(DateTime)
    estatus = Column(Boolean, default=False)
    fecha_actualizacion= Column(DateTime)
    