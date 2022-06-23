from project.users.models import User

class TestLogin:
    login_url = '/account/login'
    def test_login_with_all_field(self, client):
        data = {'email':'christ@gmail.com', 'password':'1234', 'username':'christ'}
        res = client.post('account/registration', data=data)
        assert res.status_code == 302
        user = User.query.filter_by(username=data['username']).first()

        assert user is not None
        res = client.post(self.login_url, data={'login':'christ','password':'1234'})
        assert res.status_code == 302

    def test_login_with_incorrect_password(self, client):
        data = {'email':'christ1@gmail.com', 'password':'1234', 'username':'christ1'}
        res = client.post('account/registration', data=data)
        assert res.status_code == 302
        user = User.query.filter_by(username=data['username']).first()

        assert user is not None
        res = client.post(self.login_url, data={'login':'christ1','password':'1264'})
        assert res.status_code == 200
        text = res.get_data(as_text=True)
        assert "Mot de passe incorrecte" in text

    def test_login_with_incorrect_login(self, client):
        data = {'email':'christ3@gmail.com', 'password':'1231', 'username':'christ3'}
        res = client.post('account/registration', data=data)
        assert res.status_code == 302
        user = User.query.filter_by(username=data['username']).first()

        assert user is not None
        res = client.post(self.login_url, data={'login':'incorrect login','password':'1231'})
        assert res.status_code == 200
        text = res.get_data(as_text=True)
        assert "vérifié et réessayer" in text