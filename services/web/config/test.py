from decouple import config
import os 

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = True
SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = True 