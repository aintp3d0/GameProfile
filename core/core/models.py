from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
  pass


class User(Base):
  __tablename__ = "user_account"

  id: Mapped[int] = mapped_column(primary_key=True)

  # XXX: Generated via Telegram
  token: Mapped[str] = mapped_column(String(30))

  username: Mapped[str] = mapped_column(String(30))
  fullname: Mapped[Optional[str]]

  def __repr__(self) -> str:
    return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

