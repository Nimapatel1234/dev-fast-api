from pydantic import BaseModel
from typing import List, Optional

# Schema for Users
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    class Config:
        from_attributes = True  # For compatibility with SQLAlchemy models

# Schema for Groups
class GroupBase(BaseModel):
    name: str

class GroupCreate(GroupBase):
    pass

class Group(GroupBase):
    id: int
    class Config:
        from_attributes = True

# Schema for Permissions
class PermissionBase(BaseModel):
    name: str

class PermissionCreate(PermissionBase):
    pass

class Permission(PermissionBase):
    id: int
    class Config:
        from_attributes = True

# Schema for Authors
class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    books: List["Book"] = []
    class Config:
        from_attributes = True

# Schema for Books
class BookBase(BaseModel):
    title: str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    authors: List[Author] = []
    class Config:
        from_attributes = True

# Schema for Bookshelves
class BookshelfBase(BaseModel):
    name: str

class BookshelfCreate(BookshelfBase):
    pass

class Bookshelf(BookshelfBase):
    id: int
    class Config:
        from_attributes = True

# Schema for Subjects
class SubjectBase(BaseModel):
    name: str

class SubjectCreate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: int
    class Config:
        from_attributes = True
