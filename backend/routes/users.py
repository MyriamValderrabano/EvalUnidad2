from fastapi import APIRouter,HTTPException,Depends,Request
from sqlalchemy.orm import Session
import crud.users,config.db,schemas.users,models.users
from typing import List

user = APIRouter()

models.users.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@user.get("/users/",response_model=List[schemas.users.User],tags=["Usuario"])
def read_users(skip: int = 0,limit:int=10,db:Session=Depends(get_db)):
    db_users=crud.users.get_users(db=db,skip=skip,limit=limit)
    return db_users

@user.post("/users/{id}",response_model=List[schemas.users.User],tags=["Usuario"])
def read_user(id:int,db:Session=Depends(get_db)):
    db_user=crud.users.get_user(db=db,id=id)
    if db_user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return db_user

@user.post("/users/",response_model=List[schemas.users.User],tags=["Usuario"])
def create_user(user:schemas.UserCreate,db:Session=Depends(get_db)):
    db_user=crud.users.get_user_by_usuario(db=db,id=id)
    if db_user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return db_user