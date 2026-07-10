import pytest


class TestAuthAPI:
    """Testes para autenticação"""

    def test_login_sucesso(self, client):
        response = client.post("/api/auth/login", json={
            "email": "admin@assistencia.com",
            "senha": "admin123"
        })

        assert response.status_code == 200
        data = response.json()

        assert "token" in data
        assert "user" in data

    def test_login_senha_incorreta(self, client):
        response = client.post("/api/auth/login", json={
            "email": "admin@assistencia.com",
            "senha": "senha_errada"
        })

        assert response.status_code == 401

    def test_login_email_invalido(self, client):
        response = client.post("/api/auth/login", json={
            "email": "naoexiste@email.com",
            "senha": "senha123"
        })

        assert response.status_code == 401

    def test_recuperar_senha(self, client):
        response = client.post("/api/auth/recuperar-senha", json={
            "email": "teste@email.com"
        })

        assert response.status_code in [200, 404]

    def test_logout(self, client):
        response = client.post("/api/auth/logout")

        assert response.status_code == 200