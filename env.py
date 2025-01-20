from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DEBUG: bool = False
    SECRET_KEY: str = "SECRET_KEY"
    ALLOWED_HOSTS: list[str] = []
    CSRF_TRUSTED_ORIGINS: list[str] = []
    
    class Config:
        env_file = ".env"

settings = Settings()