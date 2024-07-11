from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class Rol(Base):
    __tablename__ = "roles"
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255))
    descripcion = Column(String(255))
    created_at = Column(DateTime)
    estatus = Column(Boolean, default=False)
    