# app/schemas/user.py

from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# --- Token Schemas ---
class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class TokenPayload(BaseModel):
    sub: Optional[str] = None # 'sub' is standard for subject (user identifier)

class TokenRefresh(BaseModel):
    refresh_token: str


# --- User Schemas ---
# Base properties shared by other schemas
class UserBase(BaseModel):
    email: EmailStr = Field(..., example="user@example.com")
    full_name: Optional[str] = Field(None, example="John Doe")

# Properties to receive via API on user creation
class UserCreate(UserBase):
    password: str = Field(..., min_length=8, example="strongpassword123")

# Properties to receive via API on user update
class UserUpdate(UserBase):
    password: Optional[str] = Field(None, min_length=8, example="newstrongpassword123")
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None

# Properties stored in DB (inherits from UserBase, adds hashed_password)
class UserInDBBase(UserBase):
    id: int
    hashed_password: str
    is_active: bool = True
    is_superuser: bool = False

    class Config:
        from_attributes = True # Changed from orm_mode for Pydantic v2

# Additional properties to return via API (inherits from UserBase)
class User(UserBase):
    id: int
    is_active: bool
    is_superuser: bool

    class Config:
        from_attributes = True # For Pydantic V2, orm_mode is now from_attributes

# Schema for user stored in DB (used internally)
class UserInDB(UserInDBBase):
    pass