from datetime import datetime, date, timedelta

from sqlalchemy.orm import Session

from backend.app.models.conta_receber import ContaReceber
from backend.app.services.base_service import BaseService
from backend.app.services.auditoria_service import AuditoriaService

class ContaReceberService(BaseService):

    def __init__(self, db: Session):
        super().__init__(db)


    def gerar_conta(self, data) -> ContaReceber:

        payload = self._to_dict(data)

        # Campos obrigatórios
        if payload.get("data_vencimento") is None:
            payload["data_vencimento"] = (
                date.today() + timedelta(days=30)
            )

        if payload.get("valor_multa") is None:
            payload["valor_multa"] = 0

        if payload.get("valor_desconto") is None:
            payload["valor_desconto"] = 0


        # Se já estiver pago
        if payload.get("status", "").upper() == "PAGO":
            payload["data_pagamento"] = datetime.now()


        conta = ContaReceber(**payload)

        conta = self._commit_and_refresh(conta)
        AuditoriaService(self.db).registrar(
            funcionario_id=None,
            acao="CREATE",
            entidade="ContaReceber"
        )
        return conta

    def listar(self) -> list[ContaReceber]:
        return self.db.query(ContaReceber).all()

    def buscar_por_id(self, conta_id: int) -> ContaReceber:
        return self._get_or_raise(ContaReceber, conta_id, "Conta não encontrada")

    def atualizar(self, conta_id: int, data) -> ContaReceber:
        conta = self.buscar_por_id(conta_id)
        payload = self._to_dict(data)
        for field, value in payload.items():
            if field in {"id", "created_at", "updated_at"} or value is None:
                continue
            setattr(conta, field, value)
        self.db.commit()
        self.db.refresh(conta)
        AuditoriaService(self.db).registrar(
            funcionario_id=None,
            acao="UPDATE",
            entidade="ContaReceber"
        )
        return conta

    def marcar_como_pago(self, conta_id: int) -> ContaReceber:
        conta = self.buscar_por_id(conta_id)

        if conta.status == "PAGO":
            raise ValueError("Conta já paga")

        conta.status = "PAGO"
        conta.data_pagamento = datetime.now()
        self.db.commit()
        self.db.refresh(conta)
        AuditoriaService(self.db).registrar(
            funcionario_id=None,
            acao="UPDATE",
            entidade="ContaReceber"
        )
        return conta

    def deletar(self, conta_id: int) -> ContaReceber:
        conta = self.buscar_por_id(conta_id)
        self.db.delete(conta)
        self.db.commit()
        AuditoriaService(self.db).registrar(
            funcionario_id=None,
            acao="DELETE",
            entidade="ContaReceber"
        )
        return conta