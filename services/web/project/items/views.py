from project.mixins import AdminModelViewMixin

class ItemModelView(AdminModelViewMixin):
    column_list = [
        'name','adress', 'city','phone', 'created_at'
    ]
    form_columns = ['name','city', 'category','phone','adress','start_at', 'close_at']
    column_filters = ['city','category']


class CategoryModelView(AdminModelViewMixin):

    column_list = [
        'name'
    ]
    form_columns = ['name']

class CityModelView(AdminModelViewMixin):

    form_columns = ['name']
    
