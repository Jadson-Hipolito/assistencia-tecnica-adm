import sys
import os
import tempfile
from pathlib import Path

# Use banco de dados temporário para testes e garanta estado limpo em cada execução.
test_db_path = Path(tempfile.gettempdir()) / "assistencia_tecnica_test.sqlite"
os.environ["DATABASE_URL"] = f"sqlite:///{test_db_path}"

# Adiciona o caminho do backend ao PYTHONPATH
backend_path = Path(__file__).parent / ".."
backend_path = backend_path.resolve()
sys.path.insert(0, str(backend_path))

import pytest
from fastapi.testclient import TestClient

from backend.app.core.database import Base, engine


@pytest.fixture(autouse=True)
def setup_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield

@pytest.fixture
def client():
    """Fixture para o cliente de teste"""
    from backend.app.main import app
    return TestClient(app)

@pytest.fixture
def test_user_data():
    """Fixture com dados de usuário para teste"""
    return {
        "nome": "Teste Usuario",
        "email": "teste@email.com",
        "senha": "senha123",
        "tipo": "CLIENTE"
    }

@pytest.fixture
def test_funcionario_data():
    """Fixture com dados de funcionário para teste"""
    return {
        "nome": "Teste Funcionario",
        "email": "funcionario@email.com",
        "senha": "senha123",
        "cpf": "12345678900",
        "contato": "11999999999",
        "salario": 3000.00,
        "cargo": "TECNICO"
    }


def get_token(client):
    """Obtém token para testes"""
    response = client.post("/api/auth/login", json={
        "email": "admin@assistencia.com",
        "senha": "admin123"
    })
    if response.status_code == 200:
        return response.json()["token"]
    return "fake-jwt-token-123"
