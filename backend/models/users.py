from sqlalchemy import Column,Integer,String,Boolean,DataTime,ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class User(Base):
    __tablename__= "Users"
    
    id=Column(Integer, primary_Key=True, index=True)
    usuario= Column(String(255))
    password= Column(LONGTEXT)
    created_at= Column(DataTime)
    estatus= Column(Boolean, default=False)
    Id_persona= Column(Integer)
    #items = relationship("Item", back_populates="Owner") Clave Foranea