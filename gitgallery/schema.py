from pydantic import BaseModel


class GitUsername(BaseModel):
    " Schema for post git username "
    username: str

    class Config:
        schema_extra = {
            "example": {
                "username": "coderj001"
            }
        }
