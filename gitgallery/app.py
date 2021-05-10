#!/usr/bin/env python3
# app.py

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.database import get_db
from gitgallery.schema import GitPics, GitUsername
from gitgallery.scraper import scraper
from models import GitPhotos
from typing import Any

router = APIRouter()


@router.get('/all', status_code=status.HTTP_200_OK, response_model=List[GitPics])
def all(db: Session = Depends(get_db)) -> Any:
    gitpics = db.query(GitPhotos).filter(GitPhotos.user_id == 1).all()
    return gitpics


@router.post('/add', status_code=status.HTTP_201_CREATED, response_model=List[GitPics])
def add(request: GitUsername, db: Session = Depends(get_db)) -> Any:
    gitpic = db.query(GitPhotos).filter(GitPhotos.user_id == 1).filter(
        GitPhotos.username == request.username).first()
    gitpics = None

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
            user_id=1
        )
        db.add(gitpic)
        db.commit()
        db.refresh(gitpic)
        gitpics = db.query(GitPhotos).filter(GitPhotos.user_id == 1).all()
    else:
        gitpics = db.query(GitPhotos).filter(GitPhotos.user_id == 1).all()

    return gitpics
