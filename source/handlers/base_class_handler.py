import logging

from aiohttp import web


logger = logging.getLogger(__name__)


class BaseClassHandler(web.View):
    def __init__(self, request):
        super().__init__(request)

    async def post(self):
        return web.Response()
