from fastapi.testclient import TestClient
from backend.app.main import app
import time


def get_token(client: TestClient) -> str:
    response = client.post(
        "/api/auth/login",
        json={
            "email": "admin@assistencia.com",
            "senha": "admin123"
        }
    )
    assert response.status_code == 200
    return response.json()["token"]


def auth_headers(token: str):
    return {"Authorization": f"Bearer {token}"}


def gerar_documento_unico():
    return str(int(time.time() * 1000000))[:11]


def test_create_cliente_via_router():
    client = TestClient(app)
    token = get_token(client)

    documento = gerar_documento_unico()

    response = client.post(
        "/api/clientes/",   # 🔴 CORREÇÃO AQUI
        json={
            "nome": "Cliente Teste",
            "documento": documento,
            "endereco": "Rua Teste",
            "contato": "11999999999",
            "ativo": True,
        },
        headers=auth_headers(token)
    )

    assert response.status_code == 201

    data = response.json()
    assert "id" in data
    assert data["documento"] == documento
    assert data["nome"] == "Cliente Teste"
    assert data["ativo"] is True