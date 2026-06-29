from fastapi.testclient import TestClient

from backend.app.main import app


def test_create_cliente_via_router():
    client = TestClient(app)
    response = client.post(
        "/clientes/",
        json={
            "nome": "Cliente Teste",
            "documento": "12345678900",
            "endereco": "Rua Teste",
            "contato": "11999999999",
            "ativo": True,
        },
    )

    assert response.status_code == 201
    assert response.json()["nome"] == "Cliente Teste"