from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class Rol(Base):
    __tablename__ = "tbc_roles"
    
    ID = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(255))
    Descripcion = Column(String(255))
    Created_at = Column(DateTime)
    Estatus = Column(Boolean, default=False)
    