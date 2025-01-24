from pydantic import BaseModel
from typing import List

# Author Schemas
class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    books: List["Book"] = []
    class Config:
        from_attributes = True 

# Book Schemas
class BookBase(BaseModel):
    title: str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    authors: List[Author] = []
    class Config:
        from_attributes = True 

# User Schemas
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    class Config:
        from_attributes = True 
        
        
# Group Schemas
class GroupBase(BaseModel):
    name: str

class GroupCreate(GroupBase):
    pass

class Group(GroupBase):
    id: int
    class Config:
        from_attributes = True 

# Permission Schemas
class PermissionBase(BaseModel):
    name: str

class PermissionCreate(PermissionBase):
    pass

class Permission(PermissionBase):
    id: int
    class Config:
        from_attributes = True 

