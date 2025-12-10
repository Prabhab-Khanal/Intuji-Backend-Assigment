"""CRUD operations for Blog model."""

from sqlalchemy.orm import Session

from . import models, schemas


def get_blogs(db: Session):
    """
    Retrieve all blogs from the database.

    Args:
        db (Session): SQLAlchemy database session.

    Returns:
        list: List of Blog objects.
    """
    return db.query(models.Blog).all()


def get_blog(db: Session, blog_id: int):
    """
    Retrieve a single blog by its ID.

    Args:
        db (Session): SQLAlchemy database session.
        blog_id (int): ID of the blog to retrieve.

    Returns:
        Blog | None: Blog object if found, otherwise None.
    """
    return (
        db.query(models.Blog)
        .filter(models.Blog.id == blog_id)
        .first()
    )


def create_blog(db: Session, blog_data: schemas.BlogCreate):
    """
    Create a new blog entry.

    Args:
        db (Session): SQLAlchemy database session.
        blog_data (BlogCreate): Data required to create a blog.

    Returns:
        Blog: The newly created Blog object.
    """
    new_blog = models.Blog(
        title=blog_data.title,
        description=blog_data.description,
        category=blog_data.category,
    )

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


def update_blog(db: Session, blog_id: int, blog_data: schemas.BlogUpdate):
    """
    Update an existing blog entry.

    Args:
        db (Session): SQLAlchemy database session.
        blog_id (int): ID of the blog to update.
        blog_data (BlogUpdate): Updated blog data.

    Returns:
        Blog | None: Updated Blog object if found, otherwise None.
    """
    blog = (
        db.query(models.Blog)
        .filter(models.Blog.id == blog_id)
        .first()
    )

    if blog is None:
        return None

    blog.title = blog_data.title
    blog.description = blog_data.description
    blog.category = blog_data.category

    db.commit()
    db.refresh(blog)

    return blog
