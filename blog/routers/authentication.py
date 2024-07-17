from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from .. import schemas, Models, database, Hashing,token

get_db = database.get_db    

router = APIRouter(
    tags = ['Authentication']
)

@router.post("/login")
def login(request: schemas.login, db: Session = Depends(get_db)):
    user = db.query(Models.User).filter(Models.User.email == request.username).first()
    print(request)
    print(user)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    if not Hashing.Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Incorrect Password")
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
