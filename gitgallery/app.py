#!/usr/bin/env python3
# app.py

from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.database import get_db
from gitgallery.schema import GitUsername, Message
from gitgallery.scraper import scraper
from helper.oauth2 import get_current_user
from models import GitPhotos, User
from user.schema import UserShow

router = APIRouter()


@router.get(
    '/',
    status_code=status.HTTP_200_OK,
    response_model=Message
)
def all(
    db: Session = Depends(get_db),
    get_user: UserShow = Depends(get_current_user)
) -> Any:
    user = db.query(User).filter(User.email == get_user.email).first()
    gitpics = db.query(GitPhotos).filter(
        GitPhotos.user_id == user.id).all()
    data = dict({"data": gitpics})
    return data


@router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    response_model=Message
)
def add(
    request: GitUsername,
    db: Session = Depends(get_db),
    get_user: UserShow = Depends(get_current_user)
) -> Any:
    user = db.query(User).filter(User.email == get_user.email).first()
    gitpic = db.query(GitPhotos).filter(GitPhotos.user_id == user.id).filter(
        GitPhotos.username == request.username).first()
    gitpics = None
    message = None

    if gitpic is None:
        gitId = scraper(request.username)
        if gitId is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Github Username! {request.username} not found"
            )

        gitpic = GitPhotos(
            username=request.username,
            git_id=gitId,
            user_id=user.id
        )
        db.add(gitpic)
        db.commit()
        db.refresh(gitpic)
        gitpics = db.query(GitPhotos).filter(
            GitPhotos.user_id == user.id).all()
    else:
        gitpics = db.query(GitPhotos).filter(
            GitPhotos.user_id == user.id).all()
        message = f"{request.username} - Already present"

    data = dict({"message": message, "data": gitpics})
    return data


@router.delete(
    '/',
    status_code=status.HTTP_201_CREATED,
    response_model=Message
)
def delete(
    request: GitUsername,
    db: Session = Depends(get_db),
    get_user: UserShow = Depends(get_current_user)
) -> Any:
    user = db.query(User).filter(User.email == get_user.email).first()
    gitpic = db.query(GitPhotos).filter(GitPhotos.user_id == user.id).filter(
        GitPhotos.username == request.username).first()
    gitpics = None
    message = None

    if gitpic is None:
        gitpics = db.query(GitPhotos).filter(
            GitPhotos.user_id == user.id).all()
        message = f"{request.username} dosn't present."
    else:
        db.delete(gitpic)
        db.commit()
        gitpics = db.query(GitPhotos).filter(
            GitPhotos.user_id == user.id).all()

    data = dict({"message": message, "data": gitpics})
    return data
