from sqlalchemy.orm import Session
from .models import (
    AuthUser, AuthGroup, AuthPermission, BooksBook, BooksAuthor,
    BooksBookshelf, BooksSubject
)

# Get all users
def get_users(db: Session):
    return db.query(AuthUser).all()

# Get a single user by ID
def get_user_by_id(db: Session, user_id: int):
    return db.query(AuthUser).filter(AuthUser.id == user_id).first()

# Get all books
def get_books(db: Session):
    return db.query(BooksBook).all()

# Get all authors
def get_authors(db: Session):
    return db.query(BooksAuthor).all()

# Get all groups
def get_groups(db: Session):
    return db.query(AuthGroup).all()

# Get all permissions
def get_permissions(db: Session):
    return db.query(AuthPermission).all()

# Get all bookshelves
def get_bookshelves(db: Session):
    return db.query(BooksBookshelf).all()

# Get all subjects
def get_subjects(db: Session):
    return db.query(BooksSubject).all()


# Get all subjects
def get_all_subjects(db: Session):
    return db.query(BooksSubject).all()

# Get all book-subject relationships
def get_book_subjects(db: Session):
    return db.query(BooksBookSubjects).all()