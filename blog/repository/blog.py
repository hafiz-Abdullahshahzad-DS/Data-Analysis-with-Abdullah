from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from .. import Models, schemas

def get_all(db: Session):
    blogs = db.query(Models.Blog).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No blogs available")
    return blogs

def create(request: schemas.Blog,db: Session):
    new_blog = Models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_one(id,db: Session):
    blog = db.query(Models.Blog).filter(Models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available")
    return blog
def delBlog(id,db: Session):
    blog = db.query(Models.Blog).filter(Models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def updateBlog(id, request:schemas.Blog, db:Session):

    blog = db.query(Models.Blog).filter(Models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available")
    blog.update({'title':request.title,'body':request.body})
    db.commit()
    return 'updated'