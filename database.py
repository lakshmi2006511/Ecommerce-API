import os
<<<<<<< HEAD
# print(os.getenv())
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get("DB_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not set.")

DATABASE_URL = os.getenv("DARABASE_URL","mysql+pymysql://root:30890349@localhost:3306/ecommerce_db")
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
# provides a base class for models of sql tables
=======
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Render dashboard లో Environment Variable గా DATABASE_URL పెట్టు
DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
>>>>>>> 2aa0b8584ef1fa5e45c5d8263920750f1cda6d4
