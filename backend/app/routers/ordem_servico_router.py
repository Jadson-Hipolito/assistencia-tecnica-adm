from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.core.dependencies import get_db
from backend.app.core.dependencies_auth import require_roles
from backend.app.models.ordem_servico import OrdemServico
from backend.app.schemas.ordem_servico_schema import (
    OrdemServicoCreate,
    OrdemServicoResponse,
    OrdemServicoUpdate,
)
from backend.app.services.ordem_servico_service import OrdemServicoService

router = APIRouter(prefix="/ordens", tags=["Ordens de Serviço"])


@router.post(
    "/",
    response_model=OrdemServicoResponse,
    status_code=status.HTTP_201_CREATED,
)
def create(
    data: OrdemServicoCreate,
    db: Session = Depends(get_db),
    _: dict = Depends(require_roles("admin", "tecnico")),
):
    try:
        return OrdemServicoService(db).abrir_os(data)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get("/", response_model=List[OrdemServicoResponse])
def list_all(
    db: Session = Depends(get_db),
    _: dict = Depends(require_roles("admin", "tecnico")),
):
    return db.query(OrdemServico).all()


@router.get("/{id}", response_model=OrdemServicoResponse)
def get(
    id: int,
    db: Session = Depends(get_db),
    _: dict = Depends(require_roles("admin", "tecnico")),
):
    ordem = db.get(OrdemServico, id)
    if not ordem:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="OS não encontrada")
    return ordem


@router.put("/{id}", response_model=OrdemServicoResponse)
def update(
    id: int,
    data: OrdemServicoUpdate,
    db: Session = Depends(get_db),
    _: dict = Depends(require_roles("admin", "tecnico")),
):
    try:
        return OrdemServicoService(db).atualizar_os(id, data)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.patch("/{id}/encerrar", response_model=OrdemServicoResponse)
def encerrar(
    id: int,
    db: Session = Depends(get_db),
    _: dict = Depends(require_roles("admin", "tecnico")),
):
    try:
        return OrdemServicoService(db).finalizar_os(id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
    _: dict = Depends(require_roles("admin", "tecnico")),
):
    ordem = db.get(OrdemServico, id)
    if not ordem:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="OS não encontrada")
    db.delete(ordem)
    db.commit()
    return {"message": "Ordem de serviço cancelada com sucesso"}
