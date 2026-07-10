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


@pytest.mark.xfail(reason="Notificação endpoints ainda não implementados", strict=False)
def test_enviar_notificacao(client: TestClient):
    token = get_token(client)

    response = client.post(
        "/api/notificacoes",
        json={
            "usuario_id": 1,
            "titulo": "Aviso de teste",
            "mensagem": "Notificação de validação",
            "tipo": "INFO"
        },
        headers=auth_headers(token)
    )

    assert response.status_code in (200, 201)
    data = response.json()
    assert data["id"] == 1
    assert data["lida"] is False


@pytest.mark.xfail(reason="Notificação endpoints ainda não implementados", strict=False)
def test_listar_notificacoes(client: TestClient):
    token = get_token(client)

    response = client.get(
        "/api/notificacoes",
        headers=auth_headers(token)
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.xfail(reason="Notificação endpoints ainda não implementados", strict=False)
def test_marcar_notificacao_lida(client: TestClient):
    token = get_token(client)

    create_response = client.post(
        "/api/notificacoes",
        json={
            "usuario_id": 1,
            "titulo": "Aviso de teste",
            "mensagem": "Notificação de marcação",
            "tipo": "INFO"
        },
        headers=auth_headers(token)
    )
    assert create_response.status_code in (200, 201)
    notificacao_id = create_response.json()["id"]

    response = client.patch(
        f"/api/notificacoes/{notificacao_id}/lida",
        headers=auth_headers(token)
    )

    assert response.status_code == 200
    assert response.json().get("lida") is True
