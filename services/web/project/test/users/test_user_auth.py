from flask_login import login_url
from project.users.models import User
from flask import get_flashed_messages

class TestRegistration:

    data = {}
    registration_url = '/account/registration'

    def test_register_with_valid_field(self, client, db, session):
        data = {'email':'register@gmail.com','username':'test with valid','password':'1234'}    
        res = client.post(self.registration_url, data=data)
        assert res.status_code == 302
        assert User.query.filter_by(email='register@gmail.com').first() is not None

    def test_register_missing_password(self, client):
        test_data = {'email':'email@gmail.com','username':'tester'}

        resp = client.post(self.registration_url, data=test_data)
        assert resp.status_code == 200
        
    def test_register_missing_email(self, client):
        data = {'username':'test', 'password':'1234'}
        resp = client.post(self.registration_url, data=data)
        assert resp.status_code == 200 

    def test_register_missing_username(self, client):
        data = {'email':'test@gmail.com', 'password':'1236'}
        res = client.post(self.registration_url, data=data)
        assert res.status_code == 200
        