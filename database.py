import os
from sqlalchemy import create_engine
# connection for database
 
from sqlalchemy.orm import sessionmaker, declarative_base
 
 
# Reads DATABASE_URL from Render's Environment Variables.
# Falls back to the Aiven URL below only for local testing.
DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "mysql+pymysql://avnadmin:AVNS_yOUyno51nShOuRZ-1Q8@mysql-3be8f1b9-dhanalakshmi33.e.aivencloud.com:18494/defaultdb?ssl_mode=REQUIRED"
)
engine = create_engine(DATABASE_URL)
 
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
 
Base = declarative_base()
# provides a base class for models of sql tables
