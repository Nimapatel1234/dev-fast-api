from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..base_router import get_db  # Database session dependency
from ..models import BooksAuthor  # Reflected model for authors

router = APIRouter()

@router.get("/")
def read_authors(db: Session = Depends(get_db)):
    """Fetch all authors."""
    return db.query(BooksAuthor).all()

@router.get("/{author_id}")
def read_author_by_id(author_id: int, db: Session = Depends(get_db)):
    """Fetch a single author by ID."""
    author = db.query(BooksAuthor).filter(BooksAuthor.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

