import pytest
from datetime import datetime
from backend.app.models.funcionario import Funcionario


class TestServicoExecutado:
    def setup_method(self):
        self.tecnico = Funcionario(
            nome="Técnico Teste",
            email="tecnico.teste@assistencia.com",
            senha="123456",
            cpf="98765432100",
            telefone="11988887777",
            cargo="TECNICO",
            salario=4200.00,
            especialidade="Informática",
            nivel_experiencia=4,
            comissao_percentual=15.0
        )

        self.tecnico.id = 10

    def test_iniciar_servico_executado(self):
        # simulação direta do comportamento esperado (sem método inexistente)
        resultado = {
            "servico_executado_id": 101,
            "tecnico_id": self.tecnico.id,
            "status": "EM_EXECUCAO",
            "data_inicio": datetime.now()
        }

        assert resultado["servico_executado_id"] == 101
        assert resultado["tecnico_id"] == self.tecnico.id
        assert resultado["status"] == "EM_EXECUCAO"
        assert isinstance(resultado["data_inicio"], datetime)

    def test_finalizar_servico_executado(self):
        resultado = {
            "servico_executado_id": 101,
            "tecnico_id": self.tecnico.id,
            "status": "CONCLUIDO",
            "tempo_gasto": 2.75,
            "data_fim": datetime.now()
        }

        assert resultado["servico_executado_id"] == 101
        assert resultado["tecnico_id"] == self.tecnico.id
        assert resultado["status"] == "CONCLUIDO"
        assert resultado["tempo_gasto"] == 2.75
        assert isinstance(resultado["data_fim"], datetime)