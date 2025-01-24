from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.get("/", response_model=list[schemas.Permission])
def get_permissions(db: Session = Depends(get_db)):
    return crud.get_permissions(db)

@router.post("/", response_model=schemas.Permission)
def create_permission(permission: schemas.PermissionCreate, db: Session = Depends(get_db)):
    return crud.create_permission(db, permission)
