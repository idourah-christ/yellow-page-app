from unicodedata import name
import flask
from project.models import Category
from sqlalchemy import exc
import pytest

def test_app(app):
    assert isinstance(app, flask.Flask)

def test_create_category(db, session):
    """
    test creation of a category in the database
    """
    category = Category(name="Restaurant")
    db.session.add(category)
    db.session.commit()
     
    cat_obj = Category.query.filter_by(name="Restaurant").one()
    assert cat_obj is not None
    