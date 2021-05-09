#!/usr/bin/env python3
# app.py

from fastapi import APIRouter, status
from gitgallery.schema import GitUsername
from gitgallery.scraper import scraper

router = APIRouter()


@router.get('/all', status_code=status.HTTP_200_OK)
def all():
    return {"all": "list"}


@router.post('/add', status_code=status.HTTP_201_CREATED)
def add(request: GitUsername):
    img = scraper(request.username)
    return {
        'image': img
    }
