from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "GitGallery"
    DEBUG_MODE: bool = True


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    DB_URL: str = "sqlite:///./gitgallery.db"
    DB_NAME: str = "gitgallery"


class Setting(CommonSettings, ServerSettings, DatabaseSettings):
    pass


setting = Setting()
