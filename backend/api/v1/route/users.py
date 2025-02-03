from typing import Any

from litestar import Router, Controller, get


class UsersController(Controller):
  path = "/users"

  @get("/")
  async def get_all_users(self) -> dict[str, Any]:
    return {
      "users": [],
      "count": 0,
    }
