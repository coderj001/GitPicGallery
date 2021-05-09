#!/usr/bin/env python3
# app.py

from fastapi import APIRouter, status
from gitgallery.schema import GitUsername

router = APIRouter()


@router.get('/all', status_code=status.HTTP_200_OK)
def all():
    return {"all": "list"}


@router.post('/add', status_code=status.HTTP_201_CREATED)
def add(request: GitUsername):
    return request
