from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DEBUG: bool = False
    SECRET_KEY: str = "SECRET_KEY"
    ALLOWEDHOSTS: list[str] = []
    CSRFTRUSTEDORIGINS: list[str] = []
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()