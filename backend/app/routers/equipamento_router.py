from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.core.dependencies import get_db
from backend.app.schemas.equipamento_schema import EquipamentoCreate, EquipamentoResponse, EquipamentoUpdate
from backend.app.services.equipamento_service import EquipamentoService
from backend.app.core.dependencies_auth import require_roles

router = APIRouter(prefix="/equipamentos", tags=["Equipamentos"])


@router.post("/", response_model=EquipamentoResponse, status_code=201)
def create(
    data: EquipamentoCreate,
    db: Session = Depends(get_db),
    payload: dict = Depends(require_roles("admin", "tecnico"))
):
    try:
        executor_id = int(payload["sub"])

        return EquipamentoService(db).criar(
            data,
            executor_id
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc)
        ) from exc


@router.get("/", response_model=list[EquipamentoResponse])
def list_all(db: Session = Depends(get_db)):
    return EquipamentoService(db).listar_todos()


@router.get("/{id}", response_model=EquipamentoResponse)
def get(id: int, db: Session = Depends(get_db)):
    try:
        return EquipamentoService(db).get_by_id(id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.put("/{id}", response_model=EquipamentoResponse)
def update(
    id: int,
    data: EquipamentoUpdate,
    db: Session = Depends(get_db),
    payload: dict = Depends(require_roles("admin", "tecnico"))
):
    try:
        executor_id = int(payload["sub"])

        return EquipamentoService(db).update(
            id,
            data,
            executor_id
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc)
        ) from exc

@router.delete("/{id}", response_model=EquipamentoResponse)
def delete(
    id: int,
    db: Session = Depends(get_db),
    payload: dict = Depends(require_roles("admin", "tecnico"))
):
    try:
        funcionario_id = int(payload["sub"])

        return EquipamentoService(db).desativar(
            id,
            funcionario_id
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc)
        ) from exc