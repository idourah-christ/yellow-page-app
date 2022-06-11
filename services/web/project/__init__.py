from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
flask_migrate = Migrate()

def create_app(config=None):

    app = Flask(__name__)
    
    if config is not None:
        app.config.from_object(config)
    
    db.init_app(app)
    flask_migrate.init_app(app, db)

    from project import routes 
    app.register_blueprint(routes.app, url_prefix='/')

    from project.items import routes
    app.register_blueprint(routes.item, url_prefix='/items')
    
    return app 