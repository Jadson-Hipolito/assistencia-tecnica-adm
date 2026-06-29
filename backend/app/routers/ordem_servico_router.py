from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.core.dependencies import get_db
from backend.app.schemas.ordem_servico_schema import OrdemServicoCreate
from backend.app.services.ordem_servico_service import OrdemServicoService

router = APIRouter(prefix="/ordens", tags=["Ordens de Serviço"])


@router.post("/")
def create(data: OrdemServicoCreate, db: Session = Depends(get_db)):
    try:
        return OrdemServicoService(db).abrir_os(data)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get("/")
def list_all(db: Session = Depends(get_db)):
    return db.query(OrdemServicoService.__mro__[1].__subclasses__()[0]).all()


@router.get("/{id}")
def get(id: int, db: Session = Depends(get_db)):
    try:
        ordem = db.get(OrdemServicoService.__mro__[1].__subclasses__()[0], id)
        if not ordem:
            raise ValueError("OS não encontrada")
        return ordem
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc