from sqlalchemy.orm import Session
from .. import Models, schemas
from fastapi import HTTPException, status
from ..Hashing import Hash

def create(request: schemas.User, db: Session):
    hashed_password = Hash.bcrypt(request.password)
    new_user = Models.User(name=request.name,email=request.email,password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all(db: Session):
    users = db.query(Models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No users available")
    return users


def get_one(id,db: Session):
    user = db.query(Models.User).filter(Models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the id {id} is not available")
    return user