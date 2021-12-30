from aiohttp import web


async def healthcheck_handler(request):
    return web.Response()
