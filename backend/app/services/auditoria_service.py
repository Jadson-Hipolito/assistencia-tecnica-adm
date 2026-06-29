from datetime import datetime

from sqlalchemy.orm import Session

from backend.app.models.auditoria_log import AuditoriaLog
from backend.app.services.base_service import BaseService


class AuditoriaService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db)

    def registrar(self, funcionario_id: int, acao: str, entidade: str) -> AuditoriaLog:
        log = AuditoriaLog(
            funcionario_id=funcionario_id,
            acao=acao,
            entidade=entidade,
            data_hora=datetime.now(),
        )
        return self._commit_and_refresh(log)

    def listar(self) -> list[AuditoriaLog]:
        return self.db.query(AuditoriaLog).all()