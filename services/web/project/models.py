from project.users.views import MyAdminIndexView, MyModelView
from project import flask_admin, db
from project.users.models import User 
from project.items.models import Item, Category
from flask_admin.contrib.sqla import ModelView

flask_admin.add_view(ModelView(Category, db.session))
flask_admin.add_view(ModelView(Item, db.session))

