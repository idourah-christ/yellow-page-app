from unicodedata import name
import flask
from project.models import Category
from sqlalchemy import exc
import pytest

def test_app(app):
    assert isinstance(app, flask.Flask)


    