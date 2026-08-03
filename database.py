import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Render dashboard లో Environment Variable గా DATABASE_URL పెట్టు
DATABASE_URL = os.environ["mysql://avnadmin:AVNS_yOUyno51nShOuRZ-1Q8@mysql-3be8f1b9-dhanalakshmi33.e.aivencloud.com:18494/defaultdb"]

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
