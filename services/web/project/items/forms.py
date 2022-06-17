from flask_wtf import FlaskForm 
from wtforms import StringField, SelectField, DateField, TimeField, SubmitField, TelField, TextAreaField
from wtforms.validators import DataRequired
from project.items.models import Category


cities = [('None','Choose a city'),('Brazzaville','Brazzaville'),('Pointe-Noire','Pointe-Noire'),('Dolisie','Dolisie')]

class AddItemForm(FlaskForm):

    name = StringField("Item name", validators=[DataRequired()])
    adress = StringField("Physical address", validators=[DataRequired()])
    city = SelectField("City", choices=cities, validate_choice=False)
    phone = StringField("Phone", validators=[DataRequired()])
    description = TextAreaField("Description")
    category = SelectField("Category",choices=[], validate_choice=False)
    submit = SubmitField("Submit")