

from typing import Any, Callable, Set

from pydantic import (
    AliasChoices,
    AmqpDsn,
    BaseModel,
    Field,
    ImportString,
    PostgresDsn,
)

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  # TODO: use environment variables
  pg_dsn: PostgresDsn = 'postgresql+psycopg2://postgres:simple@localhost:5433/game_profile'


settings = Settings()
