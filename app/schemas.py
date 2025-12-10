"""Pydantic schemas for request and response validation."""

from pydantic import BaseModel


class BlogBase(BaseModel):
    """
    Base schema containing shared fields
    used for creating and updating blog entries.
    """

    title: str
    description: str
    category: str


class BlogCreate(BlogBase):
    """
    Schema for creating a new blog entry.
    Inherits all fields from BlogBase.
    """
    pass


class BlogUpdate(BlogBase):
    """
    Schema for updating an existing blog entry.
    Inherits all fields from BlogBase.
    """
    pass


class BlogOut(BlogBase):
    """
    Schema returned in API responses.
    Includes the database-generated blog ID.
    """

    id: int

    class Config:
        orm_mode = True
