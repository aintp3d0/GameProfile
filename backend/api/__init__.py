from typing import Any

from litestar import Router, Controller, get

from . import v1


api_route = Router(
  path="/api",
  route_handlers=[v1.v1_route],
)
