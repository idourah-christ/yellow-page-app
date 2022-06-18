from project.users.models import User 
import pytest
import os

@pytest.mark.skipif("CI" in os.environ and os.environ["CI"] == "True",reason="Skipping this test on Travis CI.",)
def test_create_user_instance(session):

    email = 'test1@gmail.com'
    username = 'test1'
    password = 'test2'

    user = User(username=username, email=email, password=password)
    session.add(user)
    session.commit()

    assert user.id is not None


def test_create_user_instance_without_email(session):
    
    username='test'
    password='test'
    user = User(username=username, password=password)
    session.add(user)
    session.commit()

    assert user.id is not None
    assert user.email is None

def test_create_user_instance_without_password(session):
    email='test@gmail.com'
    password='test'
    user= User(email=email,password=password)
    session.add(user)
    session.commit()

    assert user.id is not None
    assert user.password is not None 
    assert user.username is None 
    assert user.email is not None

def test_create_user_instance_without_password(session):
    email='test_without_password@gmail.com'
    username='test_without_password'
    user= User(email=email,username=username)
    session.add(user)
    session.commit()
    assert user.id is not None 
    assert user.password is None 
