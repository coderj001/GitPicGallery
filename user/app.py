#!/usr/bin/env python3
# app.py

from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.database import get_db
from helper.hashing import Hash
from helper.JWT import access_token
from models import User
from user.schema import Token, UserCreate, UserLogin, UserShow

router = APIRouter()


@router.post('/create', status_code=status.HTTP_201_CREATED, response_model=UserShow)
def create(request: UserCreate, db: Session = Depends(get_db)) -> Any:
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


@router.post('/auth', status_code=status.HTTP_200_OK, response_model=Token)
def login(request: UserLogin, db: Session = Depends(get_db)) -> Any:
    user = db.query(User).filter(User.email == request.email).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Email! {request.email} not found"
        )

    if not Hash().verify(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Please check your password"
        )
    user_dict = user.__dict__
    user_dict['access_token'] = access_token.create_access_token(
        data={"sub": user.email}
    )
    user_dict['token_type'] = "bearer"
    return user_dict
