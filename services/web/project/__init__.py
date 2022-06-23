from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_admin import Admin
from project.users.views import MyAdminIndexView


db = SQLAlchemy()
flask_migrate = Migrate()
login_manager = LoginManager()
flask_bcrypt = Bcrypt()
admin = Admin(name='yellow_app admin', template_mode='bootstrap4', index_view=MyAdminIndexView())

def create_app(config=None):

    app = Flask(__name__)
    if config is not None:
        app.config.from_object(config)
    
    db.init_app(app)
    flask_migrate.init_app(app, db)
    login_manager.init_app(app)
    admin.init_app(app)
    flask_bcrypt.init_app(app)

    register_blueprints(app)

    from project.users import models as user_model
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(user_model.User).get(user_id)
    return app 

def register_blueprints(app):
    from project import routes 
    app.register_blueprint(routes.app, url_prefix='/')
    from project.items import controlers
    app.register_blueprint(controlers.items, url_prefix='/items')
    from project.auths.controlers import auths
    app.register_blueprint(auths, url_prefix='/auths')