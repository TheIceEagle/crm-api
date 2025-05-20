# app/db/session.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings # Import the settings instance

# Create the SQLAlchemy engine
# The engine is the starting point for any SQLAlchemy application.
# It's configured with the database URL.
engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True # Checks connections for liveness before borrowing from the pool
)

# Create a SessionLocal class
# Each instance of SessionLocal will be a database session.
# The session is the primary interface for database operations.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Dependency to get a database session.
    Ensures the database session is always closed after the request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
