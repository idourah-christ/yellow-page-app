from decouple import config
import os


basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = True
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite://')
SQLALCHEMY_TRACK_MODIFICATIONS = True 
FLASK_ADMIN_SWATCH='cerulean'
ITEM_PER_PAGE = 3

