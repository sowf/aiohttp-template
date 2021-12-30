from aiohttp import web

from source.handlers import healthcheck_handler


routes = [
    web.get('/healthcheck', healthcheck_handler)
]
