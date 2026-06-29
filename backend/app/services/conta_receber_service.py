from datetime import datetime

from sqlalchemy.orm import Session

from backend.app.models.conta_receber import ContaReceber
from backend.app.services.base_service import BaseService


class ContaReceberService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db)

    def pagar_conta(self, conta_id: int) -> ContaReceber:
        conta = self._get_or_raise(ContaReceber, conta_id, "Conta não encontrada")

        if conta.status == "PAGO":
            raise ValueError("Conta já paga")

        conta.status = "PAGO"
        conta.data_pagamento = datetime.now()

        self.db.commit()
        self.db.refresh(conta)
        return conta