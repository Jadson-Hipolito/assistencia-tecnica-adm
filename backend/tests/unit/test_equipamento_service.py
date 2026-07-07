from unittest.mock import Mock
from types import SimpleNamespace

from backend.app.services.equipamento_service import EquipamentoService


def test_listar_equipamentos():

    db = Mock()

    db.query.return_value.all.return_value = []

    service = EquipamentoService(db)

    resultado = service.listar_todos()

    assert resultado == []


def test_criar_equipamento():

    db = Mock()

    service = EquipamentoService(db)

    data = {
    "nome": "Notebook",
    "tipo": "Computador",
    "marca": "Dell",
    "modelo": "Inspiron",
    "codigo": "NOTE001",
    "descricao": "Notebook teste"
}

    service._commit_and_refresh = Mock(
        side_effect=lambda x: x
    )

    resultado = service.criar(data)

    assert resultado.nome == "Notebook"
    assert resultado.tipo == "Computador"
    assert resultado.marca == "Dell"
    assert resultado.modelo == "Inspiron"


def test_update_equipamento():

    db = Mock()

    service = EquipamentoService(db)

    equipamento = Mock()
    equipamento.nome = "Antigo"
    equipamento.marca = "Antiga"

    service.get_by_id = Mock(
        return_value=equipamento
    )

    data = {
        "nome": "Novo",
        "marca": "HP",
        "id": 10,
        "created_at": None,
        "updated_at": None
    }

    resultado = service.update(1, data)

    assert resultado.nome == "Novo"
    assert resultado.marca == "HP"

    db.commit.assert_called_once()


def test_desativar_equipamento():

    db = Mock()

    service = EquipamentoService(db)

    equipamento = Mock()
    equipamento.ativo = True

    service._get_or_raise = Mock(
        return_value=equipamento
    )

    resultado = service.desativar(1)

    assert equipamento.ativo is False
    assert resultado == equipamento

    db.commit.assert_called_once()