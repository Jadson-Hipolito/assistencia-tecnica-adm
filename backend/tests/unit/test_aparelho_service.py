from unittest.mock import Mock

from backend.app.services.aparelho_service import AparelhoService


def test_listar_aparelhos():

    db = Mock()

    db.query.return_value.filter.return_value.all.return_value = []

    service = AparelhoService(db)

    resultado = service.listar_por_cliente(1)

    assert resultado == []


def test_criar_aparelho():

    db = Mock()

    service = AparelhoService(db)

    data = {
        "tipo": "Celular",
        "marca": "Samsung",
        "modelo": "A54",
        "numero_serie": "ABC123456",
        "cliente_id": 1,
        "cor": "Preto",
        "observacoes": "Teste"
    }

    service._commit_and_refresh = Mock(
        side_effect=lambda x: x
    )

    resultado = service.criar(data)

    assert resultado.tipo == "Celular"
    assert resultado.marca == "Samsung"
    assert resultado.modelo == "A54"
    assert resultado.numero_serie == "ABC123456"


def test_update_aparelho():

    db = Mock()

    service = AparelhoService(db)

    aparelho = Mock()
    aparelho.nome = "Antigo"

    service.get_by_id = Mock(
        return_value=aparelho
    )

    data = {
        "nome": "Novo",
        "marca": "Motorola",
        "id": 1,
        "created_at": None,
        "updated_at": None
    }

    resultado = service.update(1, data)

    assert resultado.nome == "Novo"
    assert resultado.marca == "Motorola"

    db.commit.assert_called_once()