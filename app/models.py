from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

# Many-to-Many Relationship for Books and Authors
books_authors = Table(
    "books_book_authors",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("books_book.id"), primary_key=True),
    Column("author_id", Integer, ForeignKey("books_author.id"), primary_key=True)
)

# Many-to-Many Relationship for Groups and Permissions
group_permissions = Table(
    "auth_group_permissions",
    Base.metadata,
    Column("group_id", Integer, ForeignKey("auth_group.id"), primary_key=True),
    Column("permission_id", Integer, ForeignKey("auth_permission.id"), primary_key=True)
)

# Many-to-Many Relationship for Users and Groups
user_groups = Table(
    "auth_user_groups",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("auth_user.id"), primary_key=True),
    Column("group_id", Integer, ForeignKey("auth_group.id"), primary_key=True)
)

# Book Model
class Book(Base):
    __tablename__ = "books_book"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    authors = relationship("Author", secondary=books_authors, back_populates="books")

# Author Model
class Author(Base):
    __tablename__ = "books_author"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    books = relationship("Book", secondary=books_authors, back_populates="authors")

# User Model
class User(Base):
    __tablename__ = "auth_user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    groups = relationship("Group", secondary=user_groups, back_populates="users")

# Group Model
class Group(Base):
    __tablename__ = "auth_group"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    users = relationship("User", secondary=user_groups, back_populates="groups")
    permissions = relationship("Permission", secondary=group_permissions, back_populates="groups")

# Permission Model
class Permission(Base):
    __tablename__ = "auth_permission"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    groups = relationship("Group", secondary=group_permissions, back_populates="permissions")
