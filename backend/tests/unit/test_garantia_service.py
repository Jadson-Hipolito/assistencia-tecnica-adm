from datetime import datetime, timedelta
import pytest

from backend.app.services.garantia_sevice import GarantiaService


class FakeOS:
    def __init__(self, data_fechamento):
        self.id = 1
        self.data_fechamento = data_fechamento


def test_calcular_fim_garantia():

    os = FakeOS(datetime(2026, 1, 1))

    resultado = GarantiaService.calcular_fim_garantia(os)

    assert resultado == datetime(2026, 4, 1)


def test_calcular_fim_garantia_sem_fechamento():

    os = FakeOS(None)

    with pytest.raises(ValueError):
        GarantiaService.calcular_fim_garantia(os)


def test_dentro_da_garantia_true():

    os = FakeOS(datetime.now() - timedelta(days=10))

    assert GarantiaService.dentro_da_garantia(os) is True


def test_dentro_da_garantia_false():

    os = FakeOS(datetime.now() - timedelta(days=100))

    assert GarantiaService.dentro_da_garantia(os) is False


def test_dentro_da_garantia_sem_data():

    os = FakeOS(None)

    assert GarantiaService.dentro_da_garantia(os) is False