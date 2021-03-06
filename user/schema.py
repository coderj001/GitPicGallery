#!/usr/bin/env python3
# schema.py
from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "coderj001",
                "email": "coderj001@mail.com",
                "password": "password"
            }
        }


class UserShow(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "coderj001@mail.com",
                "password": "password"
            }
        }


class Token(UserShow):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True
