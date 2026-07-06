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


def test_criar_ordem_servico(client: TestClient):
    token = get_token(client)

    response = client.post(
        "/api/ordens/",
        json={
            "cliente_id": 1,
            "aparelho_id": 1,
            "funcionario_id": 1,
            "descricao_problema": "Tela não liga",
            "valor_total": 250.0
        },
        headers=auth_headers(token)
    )

    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["status"] == "ABERTA"
    assert data["descricao_problema"] == "Tela não liga"


def test_listar_ordens_servico(client: TestClient):
    token = get_token(client)

    response = client.get(
        "/api/ordens/",
        headers=auth_headers(token)
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_buscar_ordem_por_id(client: TestClient):
    token = get_token(client)

    create = client.post(
        "/api/ordens/",
        json={
            "cliente_id": 2,
            "aparelho_id": 1,
            "funcionario_id": 1,
            "descricao_problema": "Não carrega",
            "valor_total": 120.0
        },
        headers=auth_headers(token)
    )

    assert create.status_code == 201
    ordem_id = create.json()["id"]

    response = client.get(
        f"/api/ordens/{ordem_id}",
        headers=auth_headers(token)
    )

    assert response.status_code == 200
    assert response.json()["id"] == ordem_id


def test_atualizar_ordem_servico(client: TestClient):
    token = get_token(client)

    create = client.post(
        "/api/ordens/",
        json={
            "cliente_id": 3,
            "aparelho_id": 1,
            "funcionario_id": 1,
            "descricao_problema": "Fone com mau contato",
            "valor_total": 80.0
        },
        headers=auth_headers(token)
    )

    assert create.status_code == 201
    ordem_id = create.json()["id"]

    response = client.put(
        f"/api/ordens/{ordem_id}",
        json={
            "descricao_problema": "Fone sem som",
            "valor_total": 90.0,
            "status": "EM_EXECUCAO"
        },
        headers=auth_headers(token)
    )

    assert response.status_code == 200
    assert response.json()["descricao_problema"] == "Fone sem som"
    assert response.json()["status"] == "EM_EXECUCAO"


def test_encerrar_ordem_servico(client: TestClient):
    token = get_token(client)

    create = client.post(
        "/api/ordens/",
        json={
            "cliente_id": 4,
            "aparelho_id": 1,
            "funcionario_id": 1,
            "descricao_problema": "Bateria viciada",
            "valor_total": 150.0
        },
        headers=auth_headers(token)
    )

    assert create.status_code == 201
    ordem_id = create.json()["id"]

    response = client.patch(
        f"/api/ordens/{ordem_id}/encerrar",
        headers=auth_headers(token)
    )

    assert response.status_code == 200
    assert response.json()["status"] == "ENCERRADA"
    assert response.json()["data_encerramento"] is not None


def test_cancelar_ordem_servico(client: TestClient):
    token = get_token(client)

    create = client.post(
        "/api/ordens/",
        json={
            "cliente_id": 5,
            "aparelho_id": 1,
            "funcionario_id": 1,
            "descricao_problema": "Teclado travando",
            "valor_total": 100.0
        },
        headers=auth_headers(token)
    )

    assert create.status_code == 201
    ordem_id = create.json()["id"]

    response = client.delete(
        f"/api/ordens/{ordem_id}",
        headers=auth_headers(token)
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Ordem de serviço cancelada com sucesso"