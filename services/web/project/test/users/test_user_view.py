class TestUserView:
    def test_login_route(self,client):
        """"""
        rep = client.get("/account/login")
        assert rep.status_code == 200
        data = rep.get_data(as_text=True)
        assert 'Connexion' in data

    def test_registration_route(self,client):

        rep = client.get("/account/registration")
        assert rep.status_code == 200
        data = rep.get_data(as_text=True)
        assert "Créer compte" in data 

    def test_login_route_incorrect_url(self,client):
        
        rep = client.get('account/logi')
        assert not rep.status_code == 200