from sqlalchemy.orm import Session

from backend.app.models.servico import Servico
from backend.app.services.base_service import BaseService


class ServicoService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db)

    def criar(self, data) -> Servico:
        servico = Servico(**self._to_dict(data))
        return self._commit_and_refresh(servico)

    def listar(self) -> list[Servico]:
        return self.db.query(Servico).all()

    def desativar(self, servico_id: int) -> Servico:
        servico = self._get_or_raise(Servico, servico_id, "Serviço não encontrado")
        servico.ativo = False
        self.db.commit()
        self.db.refresh(servico)
        return servico