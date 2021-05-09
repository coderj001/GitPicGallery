#!/usr/bin/env python3
# main.py

from fastapi import FastAPI

from database.database import engine
from gitgallery.app import router as gitgallery_router

app = FastAPI()

# engine.metadata.create_all()

app.include_router(
    gitgallery_router,
    prefix='/gallery',
    tags=['gitgallery']
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        reload=True
    )
