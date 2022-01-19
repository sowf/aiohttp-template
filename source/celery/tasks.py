import logging

from celery import Celery

import settings


celery = Celery(broker=settings.CELERY_BROKER)
logger = logging.getLogger('celery')


@celery.task
def generate_some(**kwargs):
    logger.info(f'Starting worker for params={kwargs}')
