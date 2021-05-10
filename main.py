#!/usr/bin/env python3
# main.py

from fastapi import FastAPI

from config import setting
from database.database import engine
from gitgallery.app import router as gitgallery_router
from models import Base
from user.app import router as user_router
from fastapi.staticfiles import StaticFiles


app = FastAPI()

Base.metadata.create_all(engine)


app.include_router(
    gitgallery_router,
    prefix='/gallery',
    tags=['gitgallery']
)

app.include_router(
    user_router,
    prefix='/user',
    tags=['user']
)

# index.html page
# app.mount("/", StaticFiles(directory="build"), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=setting.HOST,
        port=setting.PORT,
        reload=setting.DEBUG_MODE
    )
