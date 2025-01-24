from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..crud import get_permissions
from ..base_router import get_db

router = APIRouter()

@router.get("/")
def read_permissions(db: Session = Depends(get_db)):
    return get_permissions(db)
