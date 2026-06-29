from datetime import datetime

from sqlalchemy.orm import Session

from backend.app.models.visita_tecnica import VisitaTecnica
from backend.app.services.base_service import BaseService


class VisitaTecnicaService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db)

    def agendar(self, data) -> VisitaTecnica:
        visita = VisitaTecnica(
            ordem_servico_id=data.ordem_servico_id,
            funcionario_id=data.funcionario_id,
            data_agendamento=data.data_agendamento,
            status="AGENDADA",
        )
        return self._commit_and_refresh(visita)

    def registrar_execucao(self, visita_id: int, resultado: str) -> VisitaTecnica:
        visita = self._get_or_raise(VisitaTecnica, visita_id, "Visita técnica não encontrada")
        visita.data_realizacao = datetime.now()
        visita.resultado = resultado
        visita.status = "CONCLUIDA"
        self.db.commit()
        self.db.refresh(visita)
        return visita