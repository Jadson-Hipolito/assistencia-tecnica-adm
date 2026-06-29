from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.core.dependencies import get_db
from backend.app.core.dependencies_auth import require_roles
from backend.app.schemas.cliente_schema import ClienteCreate, ClienteResponse, ClienteUpdate
from backend.app.services.cliente_service import ClienteService

router = APIRouter(prefix="/clientes", tags=["Clientes"])


@router.post("/", response_model=ClienteResponse, status_code=201)
def create(
    data: ClienteCreate,
    db: Session = Depends(get_db),
    _: dict = Depends(require_roles("admin", "tecnico")),
):
    try:
        return ClienteService(db).create(data)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get("/", response_model=list[ClienteResponse])
def list_all(
    db: Session = Depends(get_db),
    _: dict = Depends(require_roles("admin", "tecnico")),
):
    return ClienteService(db).list_all()


@router.get("/{id}", response_model=ClienteResponse)
def get(
    id: int,
    db: Session = Depends(get_db),
    _: dict = Depends(require_roles("admin", "tecnico", "cliente")),
):
    try:
        return ClienteService(db).get_by_id(id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.put("/{id}", response_model=ClienteResponse)
def update(
    id: int,
    data: ClienteUpdate,
    db: Session = Depends(get_db),
    _: dict = Depends(require_roles("admin", "tecnico")),
):
    try:
        return ClienteService(db).update(id, data)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.delete("/{id}", response_model=ClienteResponse)
def delete(
    id: int,
    db: Session = Depends(get_db),
    _: dict = Depends(require_roles("admin")),
):
    try:
        return ClienteService(db).delete(id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc