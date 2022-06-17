from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


db = SQLAlchemy()
flask_migrate = Migrate()
flask_admin = Admin(name='yellow_page admin',template_mode='bootstrap4')
login_manager = LoginManager()
flask_bcrypt = Bcrypt()

def create_app(config=None):

    app = Flask(__name__)
    
    if config is not None:
        app.config.from_object(config)
    db.init_app(app)
    flask_migrate.init_app(app, db)
    login_manager.init_app(app)
    flask_admin.init_app(app)
    flask_bcrypt.init_app(app)

    from project.users import views as user_view
    #flask_admin.index_view=user_view.MyAdminIndexView

    from project import routes 
    app.register_blueprint(routes.app, url_prefix='/')

    from project.items import routes
    app.register_blueprint(routes.items, url_prefix='/items')

    from project.users import routes
    app.register_blueprint(routes.account, url_prefix='/account')
    
    from project.users import models as user_model
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(user_model.User).get(user_id)

    return app 