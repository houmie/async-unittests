from datetime import datetime
from functools import lru_cache

from fastapi import APIRouter
from fastapi import FastAPI

import config
from database.database import db
from routers import register


@lru_cache()
def get_settings():
    return config.Settings()


router = APIRouter()


app = FastAPI()
app.include_router(register.router)


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


@app.get("/")
async def root():
    return {
        "android": "1.0.0",
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
    }
