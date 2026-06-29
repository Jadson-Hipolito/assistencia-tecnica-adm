from backend.app.models.ordem_servico import OrdemServico
from datetime import datetime, timedelta


class GarantiaService:

    GARANTIA_PADRAO_DIAS = 90

    @staticmethod
    def calcular_fim_garantia(os: OrdemServico):
        if not os.data_fechamento:
            raise ValueError("OS não finalizada")

        return os.data_fechamento + timedelta(days=GarantiaService.GARANTIA_PADRAO_DIAS)

    @staticmethod
    def verificar_status(db, os_id: int):
        os = db.query(OrdemServico).get(os_id)

        fim = GarantiaService.calcular_fim_garantia(os)
        hoje = datetime.now()

        return {
            "os_id": os.id,
            "garantia_valida": hoje <= fim,
            "dias_restantes": (fim - hoje).days
        }

    @staticmethod
    def dentro_da_garantia(os):
        if not os.data_fechamento:
            return False

        fim = os.data_fechamento + timedelta(days=90)
        return datetime.now() <= fim