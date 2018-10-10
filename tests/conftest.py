import pytest
import logging

from playhouse.db_url import connect
from peewee_migrate import Router

from myapp import MIGRATE_DIR
from myapp.app import create as create_app
from myapp.app.db import get_objects
from myapp.app.config import Test

logger = logging.getLogger(__name__)


@pytest.fixture
def conf():
    return Test


@pytest.fixture
def app(loop, conf):
    return create_app(loop, conf=conf)


@pytest.fixture
def objects(app):
    return get_objects(app)


@pytest.fixture
def migrations(app, conf):
    database = connect(conf.database_url)
    router = Router(database, migrate_dir=MIGRATE_DIR)
    router.logger.setLevel(logging.DEBUG)
    router.run()


@pytest.fixture
def cli(app, loop, test_client, migrations):
    return loop.run_until_complete(test_client(app))
