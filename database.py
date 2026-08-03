import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not set.")

DATABASE_URL ="mysql+pymysql://avnadmin:AVNS_yOUyno51nShOuRZ-1Q8@mysql-3be8f1b9-dhanalakshmi33.e.aivencloud.com:18494/defaultdb".strip().strip('"').strip("'")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
# provides a base class for models of sql tables