import os
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Optional

load_dotenv()

class Settings(BaseModel):
    """
    Application settings.
    Values are loaded from environment variables.
    """
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "nothing")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "nothing")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "nothing")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "nothing")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "nothing")
    print(f"THIS IS THE ENV VAIRABLES FROM .ENV FILE: ----> ${POSTGRES_SERVER},${POSTGRES_PORT},${POSTGRES_USER},${POSTGRES_PASSWORD},${POSTGRES_DB}")
    
    @property
    def SQLALCHEMY_DATABASE_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
    

    SECRET_KEY: str = os.getenv("SECRET_KEY", "a_very_secret_key_please_change_this")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    REFRESH_TOKEN_EXPIRE_DAYS: int = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 7))

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()