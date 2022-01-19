import json
import logging

from aiohttp import web


logger = logging.getLogger(__name__)


class BaseClassValidator:
    def __init__(self, request):
        self.request = request

    @staticmethod
    def check_field_in_request(data, field: str):
        if field not in data:
            error_message = f"No \"{field}\" field in request."
            logger.info(error_message)
            raise web.HTTPBadRequest(
                text=json.dumps({"error": error_message}),
                content_type="application/json"
            )

    async def process_body(self):
        try:
            request_data = await self.request.json()
            logger.info(f"request_data: {request_data}")
        except json.JSONDecodeError:
            error_message = "No body in request"
            logger.info(error_message)
            raise web.HTTPBadRequest(
                text=json.dumps({"error": error_message}),
                content_type="application/json"
            )

        self.check_field_in_request(request_data, 'project_id')

        return request_data
