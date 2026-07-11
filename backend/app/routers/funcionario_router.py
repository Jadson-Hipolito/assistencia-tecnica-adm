from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.core.dependencies import get_db
from backend.app.schemas.funcionario_schema import FuncionarioCreate, FuncionarioUpdate
from backend.app.services.funcionario_service import FuncionarioService
from backend.app.core.dependencies_auth import require_roles

router = APIRouter(prefix="/funcionarios", tags=["Funcionários"])


@router.post("/")
def create(
    data: FuncionarioCreate,
    db: Session = Depends(get_db),
    payload: dict = Depends(require_roles("admin"))
):
    try:
        executor_id = int(payload["sub"])

        return FuncionarioService.create(
            db,
            data,
            executor_id
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc)
        ) from exc


@router.get("/")
def list_all(db: Session = Depends(get_db)):
    return FuncionarioService.list_all(db)


@router.get("/{id}")
def get(id: int, db: Session = Depends(get_db)):
    try:
        return FuncionarioService.get_by_id(db, id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.put("/{id}")
def update(
    id: int,
    data: FuncionarioUpdate,
    db: Session = Depends(get_db),
    payload: dict = Depends(require_roles("admin"))
):
    try:
        executor_id = int(payload["sub"])

        return FuncionarioService.update(
            db,
            id,
            data,
            executor_id
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc)
        ) from exc


@router.delete("/{id}")
def delete(
    id: int,
    db: Session = Depends(get_db),
    payload: dict = Depends(require_roles("admin"))
):
    try:
        executor_id = int(payload["sub"])

        return FuncionarioService.delete(
            db,
            id,
            executor_id
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc)
        ) from exc