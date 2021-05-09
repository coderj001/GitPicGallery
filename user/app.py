#!/usr/bin/env python3
# app.py

from fastapi import APIRouter, status, Depends
from database.database import get_db
from models import User
from sqlalchemy.orm import Session

router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK)
def all(db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == 1).first()
    print(user.username)
    return user
