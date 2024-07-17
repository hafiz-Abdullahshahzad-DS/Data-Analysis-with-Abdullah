from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, Models
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from ..repository import blog
router = APIRouter(
    tags=['blogs'],
    prefix='/blog'
)

# TO GET ALL BLOGS
@router.get("/",response_model=List[schemas.showBlog],status_code=status.HTTP_200_OK)
def all(db: Session = Depends(get_db)):
    return blog.get_all(db)

# TO CREATE A BLOG
@router.post("/",status_code=status.HTTP_201_CREATED,tags= ['blogs'])
def create(request: schemas.Blog,db: Session = Depends(get_db)):
    return blog.create(request,db)

# To get a particular blog
@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=schemas.showBlog)
def show(id,db: Session = Depends(get_db)):
    return blog.get_one(id,db)


# to delete a blog
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db: Session = Depends(get_db)):
    print(blog.delBlog(id,db))
    return blog.delBlog(id,db)

# to update a blog
@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db: Session = Depends(get_db)):
    return blog.updateBlog(id,request,db)


