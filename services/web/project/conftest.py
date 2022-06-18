
from flask_sqlalchemy import SQLAlchemy
import pytest 
from sqlalchemy import exc
from project import create_app, db as database
from dotenv import load_dotenv
from sqlalchemy import create_engine, create_mock_engine, MetaData, engine
from sqlalchemy.exc import ProgrammingError, OperationalError
import pytest
import logging
from sqlalchemy_utils.functions import database_exists,drop_database, create_database
from config.config import TestingConfig



@pytest.fixture(scope='session')
def app():
    app = create_app(config=TestingConfig)

    return app 

@pytest.fixture(scope='session')
def db(app, request):

    app = create_app(TestingConfig)
    database.app = app
    if database_exists(database.engine.url): 
        database.drop_all()
    
    database.create_all()
    def teardown():
        database.drop_all()

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


"""
  try:
      pass
    except ProgrammingError:
        logging.debug(f"Could not drop db_test, probably not exist.")
        conn.execute("ROLLBACK")
    except OperationalError:
        logging.debug("Could not drop the database because it is being used accessed by other user")
        conn.execute("ROLLBACK")
        
    logging.debug("Creating db_test database")

     logging.debug("droping the old database")
    engine = create_engine("postgresql://postgres:postgres@db/")
    conn = engine.connect()
    conn = conn.execution_options(autocommit=False)
    conn.execute(" ROLLBACK ")
    conn.execute(f"DROP DATABASE IF EXISTS db_test")
  
    conn.execute("CREATE DATABASE db_test")

    database.app = app 
    database.create_all()
"""