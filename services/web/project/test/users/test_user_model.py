from project.users.models import User 
import pytest
import os

class TestUserModelClass:
    @pytest.mark.skipif("TRAVIS" in os.environ and os.environ["TRAVIS"] == "true",reason="Skipping this test on Travis CI.",)
    def test_create_user_instance(sefl,session):

        email = 'test1@gmail.com'
        username = 'test1'
        password = 'test2'

        user = User(username=username, email=email, password=password)
        session.add(user)
        session.commit()

        assert user.id is not None

    @pytest.mark.skipif("TRAVIS" in os.environ and os.environ["TRAVIS"]=='true', 
        reason='Skipping this test on travis CI.')
    def test_create_user_instance_without_email(self,session):
        
        username='test'
        password='test'
        user = User(username=username, password=password)
        session.add(user)
        session.commit()

        assert user.id is not None
        assert user.email is None

    @pytest.mark.skipif("TRAVIS" in os.environ and os.environ["TRAVIS"]=="true",
        reason="Skipping this test on travis CI.")
    def test_create_user_instance_without_username(self, session):
        email='test@gmail.com'
        password='test'
        user= User(email=email,password=password)
        session.add(user)
        session.commit()

        assert user.id is not None
        assert user.password is not None 
        assert user.username is None 
        assert user.email is not None

    @pytest.mark.skipif("TRAVIS" in os.environ and os.environ["TRAVIS"]=="true",
        reason="Skipping this test on travis CI.")
    def test_create_user_instance_without_password(self,session):
        email='test_without_password@gmail.com'
        username='test_without_password'
        user= User(email=email,username=username)
        session.add(user)
        session.commit()
        assert user.id is not None 
        assert user.password is None 
