from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..crud import get_bookshelves
from ..base_router import get_db

router = APIRouter()

@router.get("/")
def read_bookshelves(db: Session = Depends(get_db)):
    return get_bookshelves(db)

