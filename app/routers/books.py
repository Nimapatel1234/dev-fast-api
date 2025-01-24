from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..base_router import get_db  # Correct relative import
from ..models import BooksBook  # Reflected model for books

router = APIRouter()

@router.get("/")
def read_books(db: Session = Depends(get_db)):
    """Fetch all books."""
    return db.query(BooksBook).all()

@router.get("/{book_id}")
def read_book_by_id(book_id: int, db: Session = Depends(get_db)):
    """Fetch a single book by ID."""
    book = db.query(BooksBook).filter(BooksBook.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
