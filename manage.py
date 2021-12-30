import click
import logging
import settings
import subprocess
import sys

from peewee_async import PooledPostgresqlDatabase
from peewee_migrate import Router

from source.classes import WebApp
from source import models
from source.models import LiaChannelModel, TerminatedChatModel
from source.routes import routes


logger = logging.getLogger(__name__)


@click.group()
def cli():
    pass


@cli.command()
def run():
    database = PooledPostgresqlDatabase(**settings.DB_CONFIG)
    database.bind([])
    database.set_allow_sync(False)
    app = WebApp(routes=routes)
    app.start(host=settings.HOST, port=settings.PORT)


@cli.command()
def makemigrations():
    database = PooledPostgresqlDatabase(**settings.DB_CONFIG)
    router = Router(database)

    router.create('channels', auto=models)

    database.close()

    logger.info('Migrations created successfully')


@cli.command()
def migrate():
    database = PooledPostgresqlDatabase(**settings.DB_CONFIG)
    router = Router(database)

    router.run()
    database.close()

    logger.info('Database migrated successfully')


@cli.command()
@click.option('--coverage', is_flag=True)
def test(coverage):
    args = ['pytest', 'tests']
    if coverage:
        args.append('--cov=source')
    completed_process = subprocess.run(args)
    sys.exit(completed_process.returncode)


if __name__ == '__main__':
    cli()
