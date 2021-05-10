#!/usr/bin/env python3
# app.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.database import get_db
from models import User
from user.schema import UserCreate, UserLogin, UserShow
from helper.hashing import Hash

router = APIRouter()


@router.post('/create', status_code=status.HTTP_201_CREATED, response_model=UserShow)
def create(request: UserCreate, db: Session = Depends(get_db)):
    user_username = db.query(User).filter(
        User.username == request.username).first()
    if user_username is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Username! {request.username} already present."
        )

    user_email = db.query(User).filter(User.email == request.email).first()
    if user_email is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Email! {request.email} already present."
        )

    new_user = User(
        username=request.username,
        email=request.email,
        password=Hash().bcrypt(request.password)
    )
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Internal Server Error"
        )


@router.post('/auth', status_code=status.HTTP_200_OK, response_model=UserShow)
def login(request: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Email! {request.email} not found"
        )

    if user.password != request.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Please check your password"
        )

    return user
