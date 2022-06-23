from project import create_app, db as database
import pytest
from sqlalchemy_utils.functions import database_exists
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


@pytest.fixture()
def client(app):
    return app.test_client()