from datetime import datetime, date, timedelta
from typing import List

from sqlalchemy.orm import Session

from backend.app.models.conta_receber import ContaReceber
from backend.app.services.auditoria_service import AuditoriaService


class PagamentoService:

    @staticmethod
    @staticmethod
    def create(db: Session, data) -> dict:

        conta = ContaReceber(
            ordem_servico_id=data.ordem_servico_id,

            valor_total=data.valor,
            valor_multa=0,
            valor_desconto=0,

            forma_pagamento=data.forma_pagamento,

            data_vencimento=date.today() + timedelta(days=30),

            data_pagamento=(
                datetime.now()
                if data.status.upper() == "PAGO"
                else None
            ),

            status=data.status.upper(),
        )

        db.add(conta)
        db.commit()
        db.refresh(conta)
        AuditoriaService(self.db).registrar(
            funcionario_id=None,
            acao="CREATE",
            entidade="ContaReceber"
        )
        return {
            "message": "Pagamento registrado",
            "id": conta.id
        }


    @staticmethod
    def list_all(db: Session) -> List[dict]:

        contas = db.query(ContaReceber).all()

        return [
            {
                "id": conta.id,
                "ordem_servico_id": conta.ordem_servico_id,
                "valor": float(conta.valor_total),
                "forma_pagamento": conta.forma_pagamento,
                "status": conta.status,
            }
            for conta in contas
        ]