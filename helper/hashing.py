from passlib.context import CryptContext


class Hash():
    def __init__(self):
        self.pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def bcrypt(self, password: str) -> str:
        return self.pwd_cxt.hash(password)

    def verify(self, plain_password: str, hash_password: str) -> bool:
        return self.pwd_cxt.verify(plain_password, hash_password)
