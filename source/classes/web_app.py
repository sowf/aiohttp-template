import logging

from aiohttp import web
from aiojobs.aiohttp import setup

from source.decorators import singleton
from .base_model_repository import BaseModelRepository


logger = logging.getLogger(__name__)


@singleton
class WebApp:
    def __init__(self, database, routes):
        self.app = web.Application()
        setup(self.app)
        self.app['base_model_repo'] = BaseModelRepository(database)
        self.app.add_routes(routes)
        self.app.on_startup.append(self.on_startup)
        self.app.on_shutdown.append(self.on_shutdown)

    async def on_startup(self, app):
        logger.info(f'WebApp has successfully started.')

    async def on_shutdown(self, app):
        logger.info(f'WebApp has gracefully shut down.')

    def start(self, host, port):
        logger.info(f'Starting WebApp on HOST={host} PORT={port}.')
        web.run_app(self.app, host=host, port=port)
