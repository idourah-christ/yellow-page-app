from config.config import DevelopmentConfig,ProductionConfig, get_env_db_url
from project import create_app

def test_development_config(app):
    app = create_app(DevelopmentConfig)
    DB_URL = get_env_db_url('development')
    assert app.config["DEBUG"]
    assert not app.config['TESTING']
    assert app.config["SQLALCHEMY_DATABASE_URI"] == DB_URL

def test_testing_config(app):
    DB_URL = get_env_db_url('testing')
    assert app.config['TESTING']
    assert app.config['DEBUG']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == DB_URL
  
def test_production_config(app):
    app = create_app(ProductionConfig)
    DB_URL = get_env_db_url('production')
    assert not app.config['TESTING']
    assert not app.config['DEBUG']
    assert app.config['SQLALCHEMY_DATABASE_URI'] == DB_URL