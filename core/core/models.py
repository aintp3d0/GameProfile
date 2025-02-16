from typing import Optional, List
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
  pass


class UserGame(Base):
  __tablename__ = "association__user_game"

  user_id: Mapped[int] = mapped_column(
    ForeignKey("user_account.id"), primary_key=True
  )
  game_id: Mapped[int] = mapped_column(
    ForeignKey("game.id"), primary_key=True
  )

  account_id: Mapped[str]
  banner_image: Mapped[Optional[str]]
  highlight_image: Mapped[Optional[str]]
  highlight_video: Mapped[Optional[str]]

  game: Mapped["Game"] = relationship(back_populates="users")
  user: Mapped["User"] = relationship(back_populates="games")


class User(Base):
  __tablename__ = "user_account"

  id: Mapped[int] = mapped_column(primary_key=True)

  # XXX: Generated via Telegram Bot
  token: Mapped[str] = mapped_column(String(30))

  username: Mapped[str] = mapped_column(String(30))
  fullname: Mapped[Optional[str]]

  games: Mapped[List["UserGame"]] = relationship(back_populates="game")

  def __repr__(self) -> str:
    return f"User(id={self.id!r}, name={self.username!r}, fullname={self.fullname!r})"


class Game(Base):
  __tablename__ = "game"

  id: Mapped[int] = mapped_column(primary_key=True)

  url: Mapped[str]
  name: Mapped[str]
  description: Mapped[str]
  icon_image: Mapped[str]
  banner_image: Mapped[str]

  users: Mapped[List["UserGame"]] = relationship(back_populates="user")
