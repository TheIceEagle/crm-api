from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas, models
from app.db.session import get_db
from app.core.security import get_current_active_user, get_password_hash

router = APIRouter()

@router.post("/", response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_new_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_email(db, email=user.email): raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@router.get("/me", response_model=schemas.User)
async def read_current_user_me(current_user: models.User = Depends(get_current_active_user)): return current_user

@router.put("/me", response_model=schemas.User)
async def update_current_user_me(user_update: schemas.UserUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    if user_update.role and user_update.role != current_user.role: raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Cannot change own role via this endpoint.")
    updated_user = crud.update_user(db=db, user_id=current_user.id, user_update=user_update)
    if not updated_user: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found during update")
    return updated_user

@router.put("/me/password", status_code=status.HTTP_204_NO_CONTENT)
async def update_current_user_password(password_update: schemas.UserPasswordUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    if not security.verify_password(password_update.current_password, current_user.password_hash): raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect current password")
    current_user.password_hash = get_password_hash(password_update.new_password)
    db.add(current_user); db.commit()

@router.get("/{user_id}", response_model=schemas.User)
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user

@router.get("/", response_model=List[schemas.User])
def read_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)