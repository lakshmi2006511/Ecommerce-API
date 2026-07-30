
from sqlalchemy import create_engine
# connection for database
 
from sqlalchemy.orm import sessionmaker, declarative_base
 
 
DATABASE_URL = "mysql+pymysql://root:30890349@localhost:3306/ecommerce_db"
# http://localhost:8000
engine = create_engine(DATABASE_URL)
 
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
 
Base = declarative_base()
# provides a base class for models of sql tables