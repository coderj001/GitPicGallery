#!/usr/bin/env python3
# schema.py

from pydantic import BaseModel
from datetime import datetime


class GitUsername(BaseModel):
    " Schema for post git username "
    username: str

    class Config:
        schema_extra = {
            "example": {
                "username": "coderj001"
            }
        }


class GitPics(BaseModel):
    git_id: str
    create_at: datetime

    class Config:
        orm_mode = True
