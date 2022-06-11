import pytest 
from sqlalchemy import exc
from project import create_app, db as database
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import ProgrammingError, OperationalError
import pytest
from config import test
import logging
from sqlalchemy_utils.functions import database_exists,drop_database, create_database



@pytest.fixture(scope='session')
def app():
    app = create_app(config='config.test')
    return app 

@pytest.fixture(scope='session')
def db(app, request):
    logging.debug("droping the old database")
    engine = create_engine(test.SQLALCHEMY_DATABASE_URI)
    
    try:
        # drop test_db if already exists
        if database_exists(engine.url):
            drop_database(engine.url)
    except ProgrammingError:
        logging.debug(f"Could not drop {test.TEST_DB}, probably not exist.")
    except OperationalError:
        logging.debug("Could not drop the database because it is being used accessed by other user")
    
    logging.debug("Creating db_test database")
    create_database(engine.url)
    database.app = app 
    if database_exists(engine.url):
        database.create_all()
    else:
        logging.debug(f"Error could not create table, probably {test.TEST_DB} not exist.")
    
    def teardown():
        if database_exists(engine.url):
            drop_database(engine.url)

    request.addfinalizer(teardown)

    return database

@pytest.fixture(scope='function')
def session(db, request):
    session = db.create_scoped_session()
    db.session = session 

    def teardown():
        session.remove()

    request.addfinalizer(teardown)
    return session


