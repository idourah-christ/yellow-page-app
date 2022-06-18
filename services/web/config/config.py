import os

basedir = os.path.abspath(os.path.dirname(__file__))

def get_env_variable(name):
    try:
        return os.getenv(name)
    except KeyError:
        message = "Expected env variable {} is not set".format(name)
        raise Exception(message)

def create_db_url(user, pw, url, db):
    return f"postgresql://{user}:{pw}@{url}/{db}"

def get_env_db_url(env_setting):

    if env_setting == "development":
        POSTGRES_USER = get_env_variable("DEV_POSTGRES_USER")
        POSTGRES_NAME = get_env_variable("DEV_POSTGRES_NAME")
        POSTGRES_PASSWORD = get_env_variable("DEV_POSTGRES_PASSWORD")
        POSTGRES_URL = get_env_variable("DEV_POSTGRES_URL")
    
    elif env_setting == "testing":
        POSTGRES_USER = get_env_variable("TESTING_POSTGRES_USER")
        POSTGRES_NAME = get_env_variable("TESTING_POSTGRES_NAME")
        POSTGRES_PASSWORD = get_env_variable("TESTING_POSTGRES_PASSWORD")
        POSTGRES_URL = get_env_variable("TESTING_POSTGRES_URL")

    elif env_setting == "production":
        POSTGRES_USER = get_env_variable("PROD_POSTGRES_USER")
        POSTGRES_NAME = get_env_variable("PROD_POSTGRES_NAME")
        POSTGRES_PASSWORD = get_env_variable("PROD_POSTGRES_PASSWORD")
        POSTGRES_URL = get_env_variable("PROD_POSTGRES_URL")

    return create_db_url(POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_URL, POSTGRES_NAME)

DEV_DB_URL = get_env_db_url("development")
TESTING_DB_URL = get_env_db_url("testing")
PROD_DB_URL = get_env_db_url('production')

class Config(object):
    # SQLalchemy settings

    SQLALCHEMY_DATABASE_URI = DEV_DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

    # Flask settigns
    DEBUG = False
    TESTING = False 
    SECRET_KEY = get_env_variable("SECRET_KEY")

class DevelopmentConfig(Config):

    DEBUG = True 

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = TESTING_DB_URL
    DEBUG = True 
    TESTING = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = PROD_DB_URL
