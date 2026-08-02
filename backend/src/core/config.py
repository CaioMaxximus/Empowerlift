# config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    
    api_key: str
    model_config = SettingsConfigDict(extra = "ignore")

settings = Settings()