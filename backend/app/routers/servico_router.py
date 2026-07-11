from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.schemas.servico_schema import ServicoCreate
from backend.app.services.servico_service import ServicoService
from backend.app.core.dependencies import get_db
from backend.app.core.dependencies_auth import require_roles


router = APIRouter(
    prefix="/servicos",
    tags=["Serviços"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(
    data: ServicoCreate,
    db: Session = Depends(get_db),
    payload: dict = Depends(require_roles("admin", "tecnico"))
):
    try:
        executor_id = int(payload["sub"])

        return ServicoService(db).criar(
            data,
            executor_id
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc)
        ) from exc



@router.get("/")
def list_all(
    db: Session = Depends(get_db)
):
    return ServicoService(db).listar()



@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
    payload: dict = Depends(require_roles("admin", "tecnico"))
):
    try:
        executor_id = int(payload["sub"])

        return ServicoService(db).desativar(
            id,
            executor_id
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc)
        ) from exc