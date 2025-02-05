from litestar import Litestar
from litestar.config.cors import CORSConfig

from api import api_route


cors_config = CORSConfig(allow_origins=["*"])


app = Litestar(
  route_handlers=[api_route],
  cors_config=cors_config,
)

