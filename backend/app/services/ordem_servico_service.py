from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from backend.app.models.conta_receber import ContaReceber
from backend.app.models.ordem_servico import OrdemServico
from backend.app.services.base_service import BaseService


class OrdemServicoService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db)

    def abrir_os(self, data) -> OrdemServico:
        ordem = OrdemServico(
            descricao=data.descricao,
            cliente_id=data.cliente_id,
            aparelho_id=data.aparelho_id,
            status="ABERTA",
            data_abertura=datetime.now(),
        )
        return self._commit_and_refresh(ordem)

    def finalizar_os(self, os_id: int) -> OrdemServico:
        ordem = self._get_or_raise(OrdemServico, os_id, "OS não encontrada")

        if ordem.status == "FINALIZADA":
            raise ValueError("OS já finalizada")

        ordem.status = "FINALIZADA"
        ordem.data_fechamento = datetime.now()

        conta = ContaReceber(
            ordem_servico_id=ordem.id,
            valor_total=0,
            data_vencimento=datetime.now().date() + timedelta(days=30),
            status="PENDENTE",
        )
        self.db.add(conta)
        self.db.commit()
        self.db.refresh(ordem)
        return ordem