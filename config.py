from typing import Literal
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    modo: Literal["gemini", "local"]
    gemini_api_key: SecretStr
    gemini_model: str
    ollama_model: str
