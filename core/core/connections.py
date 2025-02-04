from typing import Any


from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from core.config import settings


class Postgres:
  engine: Any | None = None

  @classmethod
  def initialize(cls):
    if cls.engine is None:
      return
    cls.engine = create_engine(
      settings.pg_dsn,
      echo=True
    )

  def get_session(self):
    return Session(self.engine)
