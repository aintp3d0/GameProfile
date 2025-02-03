from litestar import Router

from .route import route_handlers


v1_route = Router(path="/v1", route_handlers=route_handlers)
