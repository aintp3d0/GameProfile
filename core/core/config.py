import os

from pydantic import PostgresDsn, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  if not os.environ.get("IS_PRODUCTION_MODE"):
    model_config = SettingsConfigDict(env_file=".env")

  POSTGRES_DSN: PostgresDsn = Field(default=...)


settings = Settings()