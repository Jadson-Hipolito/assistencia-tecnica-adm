from fastapi import APIRouter, Depends, HTTPException, status
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
@router.post("/", status_code=201)
def gerar(data: ContaReceberCreate, db: Session = Depends(get_db)):
    try:
        return ContaReceberService(db).gerar_conta(data)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


# =========================
# LISTAR TODAS
# =========================
@router.get("/")
def listar(db: Session = Depends(get_db)):
    return ContaReceberService(db).listar()


# =========================
# BUSCAR POR ID
# =========================
@router.get("/{id}")
def buscar(id: int, db: Session = Depends(get_db)):
    try:
        return ContaReceberService(db).buscar_por_id(id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


# =========================
# ATUALIZAR CONTA
# =========================
@router.put("/{id}")
def atualizar(id: int, data: ContaReceberUpdate, db: Session = Depends(get_db)):
    try:
        return ContaReceberService(db).atualizar(id, data)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


# =========================
# MARCAR COMO PAGO
# =========================
@router.patch("/{id}/pagar")
def pagar(id: int, db: Session = Depends(get_db)):
    try:
        return ContaReceberService(db).marcar_como_pago(id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


# =========================
# DELETAR CONTA
# =========================
@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    try:
        return ContaReceberService(db).deletar(id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc