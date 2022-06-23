from email.policy import default
from sqlalchemy.ext.hybrid import hybrid_property
from project import db, flask_bcrypt, admin
from datetime import datetime
from flask_admin.contrib.sqla import ModelView
from .views import UserModelView

class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class User(Base):
    __tablename__ = "auth_user"

    # User Name
    username = db.Column(db.String(80), unique=True, nullable=False)

    # Identification Data: email & password
    email = db.Column(db.String(120), unique=True, nullable=False)

    _password = db.Column(db.String(180), nullable=False)

    is_active = db.Column(db.Boolean, default=False)

    # Authorisation Data 
    admin = db.Column(db.Boolean, default=False)
 
    @hybrid_property
    def password(self):
        return self._password
    
    @property
    def is_admin(self):
        return self.admin
    
    @password.setter
    def password(self, password):
        self._password = flask_bcrypt.generate_password_hash(password).decode('utf-8')
        
    @property
    def is_authenticated(self):
        return True 

    @property
    def is_active(self):
        return True 

    @property
    def is_anonymous(self):
        return False 

    def get_id(self):
        return self.id 

    def __unicode__(self):
        return self.username

admin.add_view(UserModelView(User, db.session))