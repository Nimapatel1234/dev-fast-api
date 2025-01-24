from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..base_router import get_db  # Database session dependency
from ..models import AuthUser  # Reflected model for users

router = APIRouter()

@router.get("/")
def read_users(db: Session = Depends(get_db)):
    """Fetch all users."""
    return db.query(AuthUser).all()

@router.get("/{user_id}")
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    """Fetch a single user by ID."""
    user = db.query(AuthUser).filter(AuthUser.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
