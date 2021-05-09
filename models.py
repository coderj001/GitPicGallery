#!/usr/bin/env python3
# models.py
from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.database import Base


class User(Base):

    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(32), unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    create_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    gitphoto = relationship("GitPhotos", back_populates="user")


class GitPhotos(Base):

    __tablename__ = 'Gallery'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    git_id = Column(String)
    create_at = Column(TIMESTAMP, nullable=False, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('Users.id'))
    user = relationship("User", back_populates="gitphoto")
