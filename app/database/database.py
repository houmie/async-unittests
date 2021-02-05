import random
import string

import databases
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import Settings

settings = Settings()

db = databases.Database(settings.sqlalchemy_database_uri)
engine = create_engine(settings.sqlalchemy_database_uri)
metadata = MetaData()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def generate_token():
    return "".join(
        random.SystemRandom().choices(string.ascii_uppercase + string.digits, k=12)
    )
