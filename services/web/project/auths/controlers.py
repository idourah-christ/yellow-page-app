from sqlalchemy import exc 
from flask import (redirect, render_template, 
    request, url_for, Blueprint, flash)
from flask_admin import helpers
from project import db
from project.users.models import User
from project.auths import forms as user_forms
import flask_login as login
import logging

auths = Blueprint('auths', __name__)

@auths.route('logout', methods=['POST', 'GET'])
def logout_view():
    login.logout_user()
    return redirect(url_for('account.login_view'))

@auths.route('login', methods=['GET','POST'])
def login_view():
    context = {}
    form = user_forms.LoginForm(request.form)
    if request.method == 'POST' and helpers.validate_form_on_submit(form):
        user = form.get_user()
        login.login_user(user)
        flash("Bienvenue {}".format(user.username),'success')
        return redirect(url_for('app.index'))

    context['page_title'] = 'LaViolette | Connexion' 
    return render_template('auths/login.html', form=form, context=context)

@auths.route('registration', methods=['GET','POST'])
def registration_view():
    context = {}
    form = user_forms.RegistrationForm(request.form)
    if request.method == 'POST' and helpers.validate_form_on_submit(form):
        user = User()
        form.populate_obj(user)
        try:
            db.session.add(user)
            db.session.commit()
            flash(f"Création du compte réussie !! Connectez-vous {form.username.data}", "success")
            return redirect(url_for('account.login_view'))
        except exc.SQLAlchemyError as e:
            flash(f"""La création de votre compte a échoué, Nous vous prions de reassayer plus tard. {e}"""
                ,'danger'
            )
            logging.debug(f"""something went wrong during registration of user: {user.username}
                The error detail can be found here : {e}"""
            )
            db.session.rollback()
          
    context['page_title'] = 'LaViolette | Nouveau compte'
    return render_template('auths/registration.html', context=context, form=form)