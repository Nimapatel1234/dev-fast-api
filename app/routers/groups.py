from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..crud import get_groups
from ..base_router import get_db

router = APIRouter()

@router.get("/")
def read_groups(db: Session = Depends(get_db)):
    return get_groups(db)
