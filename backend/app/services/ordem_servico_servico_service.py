from sqlalchemy.orm import Session

from backend.app.models.ordem_servico_servico import OrdemServicoServico
from backend.app.services.base_service import BaseService


class OrdemServicoServicoService(BaseService):
    def create(self, data) -> OrdemServicoServico:
        ordem_servico_servico = OrdemServicoServico(**self._to_dict(data))
        return self._commit_and_refresh(ordem_servico_servico)

    def list_all(self) -> list[OrdemServicoServico]:
        return self.db.query(OrdemServicoServico).all()

    def delete(self, ordem_servico_servico_id: int) -> dict:
        ordem_servico_servico = self._get_or_raise(
            OrdemServicoServico,
            ordem_servico_servico_id,
            "Equipamento usado não encontrado"
        )
        self.db.delete(ordem_servico_servico)
        self.db.commit()
        return {"message": "Equipamento usado removido com sucesso"}
