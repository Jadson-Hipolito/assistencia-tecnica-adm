import pytest
from backend.app.models.usuario import Usuario
from unittest.mock import Mock

class TestUsuarioModel:
    """Testes para o modelo Usuario"""

    def setup_method(self):
        self.usuario = Usuario(
            id=1,
            email="teste@email.com",
            senha=Usuario.criptografar_senha("senha123"),
            status="ATIVO"
        )

    def test_criar_usuario(self):
        assert self.usuario.id == 1
        assert self.usuario.email == "teste@email.com"
        assert self.usuario.status == "ATIVO"

    def test_autenticar_sucesso(self):
        assert self.usuario.autenticar("senha123") is True

    def test_autenticar_falha(self):
        assert self.usuario.autenticar("senha_errada") is False

    def test_alterar_senha(self):
        result = self.usuario.alterar_senha("nova_senha123")
        assert result is True
        assert self.usuario.autenticar("nova_senha123") is True

    def test_alterar_senha_curta(self):
        with pytest.raises(ValueError):
            self.usuario.alterar_senha("123")

    def test_desativar_usuario(self):
        self.usuario.desativar()
        assert self.usuario.status == "INATIVO"

    def test_ativar_usuario(self):
        self.usuario.desativar()
        self.usuario.ativar()
        assert self.usuario.status == "ATIVO"


class TestUsuarioAPI:
    """Testes para os endpoints de usuário"""

    def test_listar_usuarios(self, client):
        response = client.get("/api/usuarios/")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_criar_usuario_com_dados_validos(self, client, test_user_data):
        response = client.post("/api/usuarios/", json=test_user_data)
        assert response.status_code in [200, 201]
        assert "id" in response.json()

    def test_criar_usuario_email_duplicado(self, client, test_user_data):
        # Primeira criação
        client.post("/api/usuarios/", json=test_user_data)
        # Segunda com mesmo email
        response = client.post("/api/usuarios/", json=test_user_data)
        assert response.status_code == 400

    def test_buscar_usuario_por_id(self, client):
        response = client.get("/api/usuarios/1")
        assert response.status_code in [200, 404]

    def test_atualizar_usuario(self, client):
        response = client.put("/api/usuarios/1", json={"nome": "Nome Atualizado"})
        assert response.status_code in [200, 404]

    def test_desativar_usuario(self, client):
        response = client.delete("/api/usuarios/1")
        assert response.status_code in [200, 404]
