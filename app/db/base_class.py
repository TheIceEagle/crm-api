# app/db/base_class.py

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column, Integer

@as_declarative() 
class Base:
    """
    Base class for all SQLAlchemy models.
    It includes an auto-incrementing 'id' primary key by default.
    It also provides a default __tablename__ generation.
    """
    id: Column = Column(Integer, primary_key=True, index=True)
    __name__: str

    # Generate __tablename__ automatically
    # Converts CamelCase class names to snake_case table names.
    # e.g., UserItem -> user_item
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s" # Appending 's' for plural table names
