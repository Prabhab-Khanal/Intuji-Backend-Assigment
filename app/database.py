"""Database configuration and session management for the application."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# SQLite database URL
DATABASE_URL = "sqlite:///./blogs.db"

# Create SQLAlchemy engine
# `check_same_thread=False` is required for SQLite in multithreaded environments
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Create a configured "Session" class
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for all ORM models
Base = declarative_base()


def get_db():
    """
    Dependency function for obtaining a database session.

    Yields:
        Session: SQLAlchemy session used for interacting with the database.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
