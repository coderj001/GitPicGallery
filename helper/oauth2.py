from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from helper.JWT import access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/user/auth')


def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    return access_token.verify_token(token, credentials_exception)
