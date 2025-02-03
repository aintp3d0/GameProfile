from litestar import Litestar

from api import api_route


app = Litestar(
  route_handlers=[api_route],
)

