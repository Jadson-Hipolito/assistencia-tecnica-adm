import pytest
from fastapi.testclient import TestClient


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


def test_registrar_equipamento_usado(client: TestClient):
    token = get_token(client)

    response = client.post(
        "/api/equipamentos_usado",
        json={
            "servico_executado_id": 1,
            "equipamento_id": 1,
            "quantidade": 2,
            "horas_utilizadas": 1.5,
            "observacoes": "Usado para ajuste fino"
        },
        headers=auth_headers(token)
    )

    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["servico_executado_id"] == 1
    assert data["equipamento_id"] == 1
    assert data["quantidade"] == 2


def test_listar_equipamentos_usados(client: TestClient):
    token = get_token(client)

    create_response = client.post(
        "/api/equipamentos_usado",
        json={
            "servico_executado_id": 2,
            "equipamento_id": 2,
            "quantidade": 1,
            "horas_utilizadas": 0.5,
            "observacoes": "Teste listagem"
        },
        headers=auth_headers(token)
    )
    assert create_response.status_code == 201

    response = client.get(
        "/api/equipamentos_usado",
        headers=auth_headers(token)
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert any(item["id"] == create_response.json()["id"] for item in response.json())


def test_remover_equipamento_usado(client: TestClient):
    token = get_token(client)

    create_response = client.post(
        "/api/equipamentos_usado",
        json={
            "servico_executado_id": 3,
            "equipamento_id": 3,
            "quantidade": 1,
            "horas_utilizadas": 0.5,
            "observacoes": "Peça de reposição"
        },
        headers=auth_headers(token)
    )
    assert create_response.status_code == 201
    equipamento_id = create_response.json()["id"]

    delete_response = client.delete(
        f"/api/equipamentos_usado/{equipamento_id}",
        headers=auth_headers(token)
    )

    assert delete_response.status_code == 200
    assert delete_response.json().get("message") == "Equipamento usado removido com sucesso"
