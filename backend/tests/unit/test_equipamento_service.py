from unittest.mock import Mock

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

    data = Mock()
    data.__dict__ = {
        "nome": "Notebook",
        "marca": "Dell"
    }

    service._commit_and_refresh = Mock(
        side_effect=lambda x: x
    )

    resultado = service.criar(data)

    assert resultado.nome == "Notebook"