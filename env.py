from pydantic_settings import BaseSettings, ForceDecode, NoDecode
from pydantic.fields import FieldInfo
from typing import Any
class Settings(BaseSettings):
    DEBUG: bool = False
    SECRET_KEY: str = "SECRET_KEY"
    ALLOWEDHOSTS: list[str] = []
    CSRFTRUSTEDORIGINS: list[str] = []
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()