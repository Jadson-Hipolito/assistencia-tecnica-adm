import pytest
from fastapi.testclient import TestClient


def test_dashboard_resumo(client: TestClient):
    response = client.get("/api/relatorios/dashboard/resumo")

    assert response.status_code == 200
    data = response.json()
    assert "resumo" in data
    assert "total_clientes" in data["resumo"]
    assert "total_usuarios" in data["resumo"]
    assert "total_funcionarios" in data["resumo"]
    assert "gerado_em" in data


def test_relatorio_usuarios(client: TestClient):
    response = client.get("/api/relatorios/usuarios")

    assert response.status_code == 200
    data = response.json()
    assert data["tipo"] == "usuarios"
    assert isinstance(data["usuarios"], list)
    assert "total" in data
    assert "gerado_em" in data


def test_relatorio_clientes(client: TestClient):
    response = client.get("/api/relatorios/clientes")

    assert response.status_code == 200
    data = response.json()
    assert data["tipo"] == "clientes"
    assert isinstance(data["clientes"], list)
    assert "total" in data
    assert "gerado_em" in data


def test_relatorio_funcionarios(client: TestClient):
    response = client.get("/api/relatorios/funcionarios")

    assert response.status_code == 200
    data = response.json()
    assert data["tipo"] == "funcionarios"
    assert isinstance(data["funcionarios"], list)
    assert "total" in data
    assert "gerado_em" in data


def test_relatorio_completo(client: TestClient):
    response = client.get("/api/relatorios/completo")

    assert response.status_code == 200
    data = response.json()
    assert "resumo_geral" in data
    assert "total_geral" in data["resumo_geral"]
    assert "gerado_em" in data
