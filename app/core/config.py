from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional


class Settings(BaseSettings):
    app_name: str = "Health Microservice API"
    debug: bool = False
    version: str = "1.0.0"

    # Database
    database_url: str = Field(..., env="DATABASE_URL")

    # JWT
    secret_key: str = Field(..., env="SECRET_KEY")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # CORS
    backend_cors_origins: list[str] = [
        "http://localhost:3000",
        "http://localhost:5000",
        "http://localhost:8080",
    ]

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
