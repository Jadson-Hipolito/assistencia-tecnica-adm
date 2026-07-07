from unittest.mock import Mock

from backend.app.services.visita_tecnica_service import VisitaTecnicaService


def test_listar_visitas():

    db = Mock()

    db.query.return_value.all.return_value = []

    service = VisitaTecnicaService(db)

    resultado = service.listar_todas()

    assert resultado == []


def test_agendar_visita():

    db = Mock()

    service = VisitaTecnicaService(db)

    data = Mock()

    data.ordem_servico_id = 1
    data.funcionario_id = 1
    data.data_agendamento = "2026-07-07"

    service._commit_and_refresh = Mock(
        side_effect=lambda x: x
    )

    resultado = service.agendar(data)

    assert resultado.status == "AGENDADA"