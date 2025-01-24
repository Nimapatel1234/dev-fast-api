from sqlalchemy.orm import Session
from . import models, schemas

# Books
def get_books(db: Session):
    return db.query(models.Book).all()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(title=book.title)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# Authors
def get_authors(db: Session):
    return db.query(models.Author).all()

def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(name=author.name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

# Users
def get_users(db: Session):
    return db.query(models.User).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Groups
def get_groups(db: Session):
    return db.query(models.Group).all()

def get_group_by_id(db: Session, group_id: int):
    return db.query(models.Group).filter(models.Group.id == group_id).first()

def create_group(db: Session, group: schemas.GroupCreate):
    db_group = models.Group(name=group.name)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

# Permissions
def get_permissions(db: Session):
    return db.query(models.Permission).all()

def get_permission_by_id(db: Session, permission_id: int):
    return db.query(models.Permission).filter(models.Permission.id == permission_id).first()

def create_permission(db: Session, permission: schemas.PermissionCreate):
    db_permission = models.Permission(name=permission.name)
    db.add(db_permission)
    db.commit()
    db.refresh(db_permission)
    return db_permission
