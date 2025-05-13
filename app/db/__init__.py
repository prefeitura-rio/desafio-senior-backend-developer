#from decouple import config
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#DB_URL = config('DB_URL')
Base = declarative_base()
DB_URL = "postgresql://fastapi_test:fastapi_test_password@localhost:5432/db"

#from sqlmodel import create_engine, SQLModel, Session
#from app import models 


SQLALCHEMY_DATABASE_URL = (
    DB_URL
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionLocal = sessionmaker(bind=engine)


""" def init_db():
    Base.metadata.create_all(bind=engine) """
