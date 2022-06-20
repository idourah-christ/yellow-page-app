import email
from sqlalchemy import exc 
from flask import (redirect, render_template, 
    request, url_for, Blueprint, flash)
from flask_admin import helpers
from project import db
from project.users.models import User
from project.users import forms as user_forms
import flask_login as login
import logging

account = Blueprint('account', __name__)

@account.route('login', methods=['GET','POST'])
def login_view():
    context = {}
    form = user_forms.LoginForm(request.form)
    if request.method == 'POST' and helpers.validate_form_on_submit(form):
        user = form.get_user()
        login.login_user(user)
        flash("Bienvenue {user.username}",'success')
        return redirect(url_for('app.home'))

    context['page_title'] = 'LaViolette | Connexion' 
    return render_template('account/login.html', form=form, context=context)

@account.route('registration', methods=['GET','POST'])
def registration_view():
    context = {}
    form = user_forms.RegistrationForm(request.form)
    if request.method == 'POST' and helpers.validate_form_on_submit(form):
        user = User()
        form.populate_obj(user)
        try:
            db.session.add(user)
            db.session.commit()
            flash("Création du compte réussie !! Connectez-vous {form.username}", "success")
            return redirect(url_for('account.login_view'))
        except exc.SQLAlchemyError as e:
            flash
            ("""
                La création de votre compte a échoué, Nous vous prions de reassayer plus tard. {e}"""
                ,'danger'
            )
            logging.debug
            ("""
                something went wrong during registration of user: {user.username}
                The error detail can be found here : {e}
             """
            )
            db.session.rollback()
          
    context['page_title'] = 'LaViolette | Nouveau compte'
    return render_template('account/registration.html', context=context, form=form)