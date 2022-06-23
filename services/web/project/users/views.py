from ast import Pass
from flask_admin.contrib import sqla
from flask_admin import helpers, expose
import flask_login as login
import flask_admin as admin
from flask import redirect, request, url_for
from project.mixins import AdminModelViewMixin
from wtforms.fields import PasswordField


class MyModelView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated

class MyAdminIndexView(admin.AdminIndexView):

    @expose('/')
    def index(self):
        if not (login.current_user.is_authenticated and login.current_user.is_admin):
            return redirect(url_for('.login'))
        return self.render('admin/index.html')

   
    @expose('/login/', methods=['GET','POST'])
    def login(self):
        from .forms import LoginForm
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)

        if (login.current_user.is_authenticated and login.current_user.is_admin):
            return redirect(url_for('.index'))

        self._template_args['form'] = form 
        context = {'page_title':'LaViolette | admin'}
        return self.render('admin/login.html', form=form, context=context)

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))

class UserModelView(AdminModelViewMixin):

    column_list = [
        'email', 'username','is_active', 'date_created', 'is_admin'
    ]
    column_searchable_list = ['email', 'username']
    column_filters = ['username', 'date_created']

    form_columns = ['email','username', 'password', 'admin']
    form_extra_fields = {
        'password': PasswordField('New password')
    }
  
    