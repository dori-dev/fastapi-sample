from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

user = 'postgres'
password = 1234
db_name = 'ketab'
# SQLALCHEMY_DATABASE_URL = f'postgresql://{user}:{password}@postgresserver/{db_name}'

SQLALCHEMY_DATABASE_URL = 'sqlite:///./ketab.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread": False,
    },
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()
