import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # Environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")



    class Config:
        case_sensitive = True
        env_file = ".env"