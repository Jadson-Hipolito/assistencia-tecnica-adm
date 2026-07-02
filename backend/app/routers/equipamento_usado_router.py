from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.core.dependencies import get_db
from backend.app.schemas.equipamento_schema import EquipamentoResponse
from backend.app.schemas.ordem_servico_servico_schema import OrdemServicoServicoCreate, OrdemServicoServicoResponse
from backend.app.services.ordem_servico_servico_service import OrdemServicoServicoService

router = APIRouter(prefix="/equipamentos_usado", tags=["Equipamentos Usados"])


@router.post("", response_model=OrdemServicoServicoResponse, status_code=201)
@router.post("/", response_model=OrdemServicoServicoResponse, status_code=201)
def create(data: OrdemServicoServicoCreate, db: Session = Depends(get_db)):
    try:
        return OrdemServicoServicoService(db).create(data)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get("", response_model=list[OrdemServicoServicoResponse])
@router.get("/", response_model=list[OrdemServicoServicoResponse])
def list_all(db: Session = Depends(get_db)):
    return OrdemServicoServicoService(db).list_all()


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    try:
        return OrdemServicoServicoService(db).delete(id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
