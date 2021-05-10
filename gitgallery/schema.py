#!/usr/bin/env python3
# schema.py

from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class GitUsername(BaseModel):
    username: str

    class Config:
        schema_extra = {
            "example": {
                "username": "coderj001"
            }
        }


class GitPics(BaseModel):
    username: str
    git_id: str
    create_at: datetime

    class Config:
        orm_mode = True


class Message(BaseModel):
    message: Optional[str] = None
    data: List[GitPics] = []

    class Config:
        orm_mode = True
