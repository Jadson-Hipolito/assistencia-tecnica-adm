from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.schemas.pagamento_schema import (
    PagamentoCreate,
    PagamentoUpdate
)
from backend.app.services.pagamento_service import PagamentoService
from backend.app.core.dependencies import get_db
from backend.app.models.conta_receber import ContaReceber


router = APIRouter(
    prefix="/pagamentos",
    tags=["Pagamentos"]
)


@router.post("/")
def create(data: PagamentoCreate, db: Session = Depends(get_db)):
    return PagamentoService.create(db, data)


@router.get("/")
def list_all(db: Session = Depends(get_db)):
    return PagamentoService.list_all(db)


@router.delete("/{pagamento_id}")
def delete_pagamento(
    pagamento_id: int,
    db: Session = Depends(get_db)
):
    conta = db.query(ContaReceber).filter(
        ContaReceber.id == pagamento_id
    ).first()

    if not conta:
        return {
            "error": "Pagamento não encontrado"
        }

    db.delete(conta)
    db.commit()

    return {
        "message": "Pagamento excluído com sucesso"
    }

@router.put("/{pagamento_id}")
def update_pagamento(
    pagamento_id: int,
    data: PagamentoUpdate,
    db: Session = Depends(get_db)
):

    conta = db.query(ContaReceber).filter(
        ContaReceber.id == pagamento_id
    ).first()


    if not conta:
        return {
            "error": "Pagamento não encontrado"
        }


    if data.valor is not None:
        conta.valor = data.valor


    if data.status is not None:
        conta.status = data.status


    if data.forma_pagamento is not None:
        conta.forma_pagamento = data.forma_pagamento


    db.commit()
    db.refresh(conta)


    return conta