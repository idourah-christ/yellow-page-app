from flask_admin.contrib import sqla
from flask_admin import helpers, expose
import flask_login as login
import flask_admin as admin
from flask import redirect, render_template, request, url_for, Blueprint


class MyModelView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated

class MyAdminIndexView(admin.AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

   
    @expose('/login/', methods=['GET','POST'])
    def login_view(self):
        from .forms import LoginForm
        form = LoginForm(request.data)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))
        
        self._template_args['form'] = form 
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))
