from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "postgresql://user:password@postgres/db"

# Create database engine
engine = create_engine(DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(bind=engine)

# Ensure tables are created
def init_db():
    """Creates all tables in the database."""
    Base.metadata.create_all(engine)
