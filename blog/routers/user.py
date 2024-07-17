from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, Models
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from ..repository import user
router = APIRouter(
    tags=['users'],
    prefix="/user"
)

# to create a user
@router.post("/",status_code=status.HTTP_201_CREATED)
def create_user(requuest:schemas.User,db: Session = Depends(get_db)):
    return user.create(requuest,db)

@router.get("/",status_code=status.HTTP_200_OK,response_model=List[schemas.ShowUser])
def shows_users(db: Session = Depends(get_db)):
    return user.get_all(db)


@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=schemas.ShowUser)
def show_user(id,db: Session = Depends(get_db)):
    return user.get_one(id,db)