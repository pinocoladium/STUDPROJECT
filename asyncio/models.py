import os

from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_DB = os.getenv("PG_DB")
PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")

PG_DSN = f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"

engine = create_async_engine(PG_DSN)
Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()


class SwapiPeople(Base):
    __tablename__ = "swapi_people"

    id = Column(Integer, primary_key=True)
    id_personage = Column(Integer, nullable=False)
    birth_year = Column(String, nullable=False)
    eye_color = Column(String, nullable=False)
    films = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    hair_color = Column(String, nullable=False)
    height = Column(String, nullable=False)
    homeworld = Column(String, nullable=False)
    mass = Column(String, nullable=False)
    name = Column(String, nullable=False)
    skin_color = Column(String, nullable=False)
    species = Column(String)
    starships = Column(String, nullable=False)
    vehicles = Column(String, nullable=False)
