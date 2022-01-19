import logging

from peewee_async import Manager
from playhouse.shortcuts import model_to_dict
from uuid import uuid4

from source.exceptions import DBUpdateError
from source.models import BaseModel


logger = logging.getLogger(__name__)


class BaseModelRepository:
    """
    Class for interaction with DB
    Created for CRUD operations with BaseModel
    """
    def __init__(self, database):
        self.session = Manager(database)
        self.database = database

    async def find(self, **params):
        try:
            db_obj = await self.session.get(BaseModel, **params)
        except BaseModel.DoesNotExist:
            return False

        return model_to_dict(db_obj)

    async def set(self, **kwargs):
        try:
            existing_channel = await self.session.get(
                BaseModel,
                char_field=kwargs.get('char_field')
            )

            if await self.session.delete(existing_channel) != 1:
                raise DBUpdateError(f'Database updated with errors: {kwargs}')
        except BaseModel.DoesNotExist:
            pass

        created_channel = await self.session.create(BaseModel, **kwargs, id=str(uuid4()))

        return model_to_dict(created_channel)

    async def delete(self, char_field):
        try:
            data = await self.session.get(
                BaseModel,
                char_field=char_field
            )

            if await self.session.delete(data) != 1:
                raise DBUpdateError(f'Database updated with errors: {data}')
        except BaseModel.DoesNotExist:
            logger.warning(f'Data does not exist: char_field={char_field}')

        return True
