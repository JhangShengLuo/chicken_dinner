import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Lifetime Financial Consulting AI"
    # Use sqlite by default for local dev outside of docker, postgres inside docker
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./financial_test.db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
