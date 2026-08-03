import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Load environment variables for local testing
load_dotenv()

# Get the database URL from Render Environment Variables
# If running locally and DB_URL is missing, it falls back to your local MySQL database
DATABASE_URL = os.environ.get(
    "DATABASE_URL", 
    os.environ.get("DB_URL", "mysql+pymysql://root:30890349@localhost:3306/ecommerce_db")
)

if not DATABASE_URL:
    raise RuntimeError("Database connection string is not set.")

# Create the engine with pool_pre_ping to prevent disconnected connection errors on production
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Provides a base class for models of SQL tables
Base = declarative_base()

