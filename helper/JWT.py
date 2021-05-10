from datetime import datetime, timedelta

from jose import JWTError, jwt

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1670


class AccessToken:
    def __init__(self):
        self.__algorithm = ALGORITHM
        self.__secret_key = SECRET_KEY
        self.__token_expire = ACCESS_TOKEN_EXPIRE_MINUTES

    def create_access_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=self.__token_expire)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode,
            self.__secret_key,
            algorithm=self.__algorithm
        )
        return encoded_jwt


access_token = AccessToken()
