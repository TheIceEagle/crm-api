# app/models/user.py

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship # If you plan to add relationships later

from app.db.base_class import Base # Import the Base class we defined

class User(Base):
    """
    User model for storing user information.
    """
    __tablename__ = "users" # Explicitly defining tablename, can also use Base's auto-generation

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, index=True, nullable=True)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)

    # Example of a relationship (if you had an Item model, for instance)
    # items = relationship("Item", back_populates="owner")

    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}')>"
