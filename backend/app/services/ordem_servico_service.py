from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from backend.app.models.conta_receber import ContaReceber
from backend.app.models.ordem_servico import OrdemServico
from backend.app.services.base_service import BaseService
from backend.app.services.auditoria_service import AuditoriaService


class OrdemServicoService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db)

    def abrir_os(self, data, executor_id: int) -> OrdemServico:
        ordem = OrdemServico(
            descricao_problema=data.descricao_problema,
            cliente_id=data.cliente_id,
            aparelho_id=data.aparelho_id,
            funcionario_id=data.tecnico_id,
            valor_total=data.valor_total or 0,
            status="ABERTA",
            data_abertura=datetime.now(),
        )
        ordem = self._commit_and_refresh(ordem)


        AuditoriaService(self.db).registrar(
            funcionario_id=executor_id,
            acao="CREATE",
            entidade="OrdemServico"
        )


        return ordem

    def finalizar_os(self, os_id: int, executor_id: int) -> OrdemServico:
        ordem = self._get_or_raise(OrdemServico, os_id, "OS não encontrada")

        if ordem.status == "ENCERRADA":
            raise ValueError("OS já encerrada")

        ordem.status = "ENCERRADA"
        ordem.data_fechamento = datetime.now()

        conta = ContaReceber(
            ordem_servico_id=ordem.id,
            valor_total=ordem.valor_total or 0,
            data_vencimento=datetime.now().date() + timedelta(days=30),
            status="PENDENTE",
        )
        self.db.add(conta)
        self.db.commit()
        self.db.refresh(ordem)
        AuditoriaService(self.db).registrar(
            funcionario_id=executor_id,
            acao="DELETE",
            entidade="OrdemServico"
        )
        return ordem

    def atualizar_os(self, os_id: int, data, executor_id: int) -> OrdemServico:
        ordem = self._get_or_raise(OrdemServico, os_id, "OS não encontrada")

        if data.descricao_problema is not None:
            ordem.descricao_problema = data.descricao_problema
        if data.valor_total is not None:
            ordem.valor_total = data.valor_total
        if data.status is not None:
            ordem.status = data.status
            if data.status == "ENCERRADA" and ordem.data_fechamento is None:
                ordem.data_fechamento = datetime.now()
        if data.tecnico_id is not None:
            ordem.funcionario_id = data.tecnico_id

        self.db.commit()
        self.db.refresh(ordem)
        AuditoriaService(self.db).registrar(
            funcionario_id=executor_id,
            acao="UPDATE",
            entidade="OrdemServico"
        )
        return ordem
