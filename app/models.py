"""SQLAlchemy ORM models for the Blog application."""

from sqlalchemy import Column, Integer, String

from .database import Base


class Blog(Base):
    """Database model representing a blog entry."""

    __tablename__ = "blogs"  # SQLite table name

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=False
    )

    category = Column(
        String,
        nullable=False
    )  # Single category per blog
