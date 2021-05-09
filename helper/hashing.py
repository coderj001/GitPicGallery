#!/usr/bin/env python3
# hashing.py

from passlib.context import CryptContext


class Hash:
    def __init__(self):
        self.pwd_context = CryptContext(
            schemes=["bycrypt"],
            deprecated="auto"
        )

    def generate_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def varify_password(self, plain_password: str, hashed_password: str) -> str:
        return self.pwd_context.verify(plain_password, hashed_password)
