"""Main FastAPI application with routes for Blog CRUD operations."""

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import engine, get_db


# Create all database tables at startup
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI()


@app.get("/blogs", response_model=list[schemas.BlogOut])
def read_blogs(db: Session = Depends(get_db)):
    """
    Retrieve all blogs.

    Args:
        db (Session): Database session.

    Returns:
        list[BlogOut]: List of available blogs.
    """
    return crud.get_blogs(db)


@app.get("/blogs/{blog_id}", response_model=schemas.BlogOut)
def read_blog(blog_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a blog by its ID.

    Args:
        blog_id (int): Blog ID.
        db (Session): Database session.

    Raises:
        HTTPException: If the blog is not found.

    Returns:
        BlogOut: Blog data.
    """
    blog = crud.get_blog(db, blog_id)

    if blog is None:
        raise HTTPException(
            status_code=404,
            detail="Blog not found"
        )

    return blog


@app.post("/blogs", response_model=schemas.BlogOut)
def create_new_blog(
    blog: schemas.BlogCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new blog entry.

    Args:
        blog (BlogCreate): Blog details.
        db (Session): Database session.

    Returns:
        BlogOut: Created blog.
    """
    return crud.create_blog(db, blog)


@app.put("/blogs/{blog_id}", response_model=schemas.BlogOut)
def update_existing_blog(
    blog_id: int,
    blog: schemas.BlogUpdate,
    db: Session = Depends(get_db)
):
    """
    Update an existing blog.

    Args:
        blog_id (int): Blog ID.
        blog (BlogUpdate): Updated blog details.
        db (Session): Database session.

    Raises:
        HTTPException: If the blog does not exist.

    Returns:
        BlogOut: Updated blog.
    """
    updated_blog = crud.update_blog(db, blog_id, blog)

    if updated_blog is None:
        raise HTTPException(
            status_code=404,
            detail="Blog not found"
        )

    return updated_blog
