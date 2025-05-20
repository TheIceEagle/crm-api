# app/db/init_db.py

from sqlalchemy.orm import Session
from app.db.base_class import Base
from app.db.session import engine # Import engine from session.py

# make sure all SQL Alchemy models are imported (app.models) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28

from app.models.user import User # Import your models here

def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But for simplicity, we are creating them directly here
    Base.metadata.create_all(bind=engine)
    # You can add initial data creation here if needed
    # For example, create a superuser
