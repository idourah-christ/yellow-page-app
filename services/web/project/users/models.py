from sqlalchemy.ext.hybrid import hybrid_property
from project import db, flask_bcrypt, flask_admin
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"

    id= db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    _password = db.Column(db.String(180))
    create_at = db.Column(db.DateTime, default=datetime.utcnow)

    @hybrid_property
    def password(self):
        return self._password
    
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

from flask_admin.contrib.sqla import ModelView
flask_admin.add_view(ModelView(User, db.session))