from wtforms import form, fields, validators
from project.users import models as user_model
from project import db, flask_bcrypt
import re 

class LoginForm(form.Form):
    login = fields.StringField(validators=[validators.DataRequired()])
    password = fields.PasswordField('Mot de passe',validators=[validators.DataRequired()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError(
                f"""
                { self.login.data } n'existe pas vérifié et réessayer 
                """
            )
        
        if not (flask_bcrypt.check_password_hash(user.password, self.password.data)):
            raise validators.ValidationError("Mot de passe incorrecte")

    def get_user(self):
        return db.session.query(user_model.User)\
                .filter(user_model.User.username==self.login.data).first()

class RegistrationForm(form.Form):
    username = fields.StringField('Nom utilisateur',validators=[validators.DataRequired()])
    email = fields.EmailField('Adresse électronique',validators=[validators.DataRequired()])
    password = fields.PasswordField('Mot de passe',validators=[validators.DataRequired()])

    def validate_username(self, field):
        if db.session.query(user_model.User).filter_by(username=self.username.data).count() > 0:
            raise validators.ValidationError(f'Un compte existe déjà avec {self.username.data}')

    def validate_email(self, field):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if db.session.query(user_model.User).filter_by(email=self.email.data).count() > 0:
            raise validators.ValidationError(f"Un compte existe déjà avec {self.email.data}")

        if not (re.fullmatch(regex, self.email.data)):
            raise validators.ValidationError(f"{self.email.data} n'est pas correcte")   

    