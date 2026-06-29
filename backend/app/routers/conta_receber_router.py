from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.core.dependencies import get_db
from backend.app.schemas.conta_receber_schema import (
    ContaReceberCreate,
    ContaReceberUpdate,
)
from backend.app.services.conta_receber_service import ContaReceberService

router = APIRouter(prefix="/contas-receber", tags=["Contas a Receber"])


# =========================
# GERAR CONTA A RECEBER
# =========================
@router.post("/")
def gerar(data: ContaReceberCreate, db: Session = Depends(get_db)):
    return ContaReceberService.gerar(db, data)


# =========================
# LISTAR TODAS
# =========================
@router.get("/")
def listar(db: Session = Depends(get_db)):
    return ContaReceberService.listar(db)


# =========================
# BUSCAR POR ID
# =========================
@router.get("/{id}")
def buscar(id: int, db: Session = Depends(get_db)):
    conta = ContaReceberService.buscar_por_id(db, id)

    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    return conta


# =========================
# ATUALIZAR CONTA
# =========================
@router.put("/{id}")
def atualizar(id: int, data: ContaReceberUpdate, db: Session = Depends(get_db)):
    return ContaReceberService.atualizar(db, id, data)


# =========================
# MARCAR COMO PAGO
# =========================
@router.patch("/{id}/pagar")
def pagar(id: int, db: Session = Depends(get_db)):
    return ContaReceberService.marcar_como_pago(db, id)


# =========================
# DELETAR CONTA
# =========================
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    return ContaReceberService.deletar(db, id)