from typing import List
from sqlalchemy.orm import Session
from backend.app.models.conta_receber import ContaReceber


class PagamentoService:
    @staticmethod
    def create(db: Session, data) -> dict:
        conta = ContaReceber(
            ordem_servico_id=data.ordem_servico_id,
            valor_total=data.valor,
            status="PAGO",
        )
        db.add(conta)
        db.commit()
        db.refresh(conta)
        return {"message": "Pagamento registrado", "id": conta.id}

    @staticmethod
    def list_all(db: Session) -> List[dict]:
        return []