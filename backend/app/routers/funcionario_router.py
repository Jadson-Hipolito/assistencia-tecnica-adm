from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.core.dependencies import get_db
from backend.app.schemas.funcionario_schema import FuncionarioCreate, FuncionarioUpdate
from backend.app.services.funcionario_service import FuncionarioService

router = APIRouter(prefix="/funcionarios", tags=["Funcionários"])


@router.post("/")
def create(data: FuncionarioCreate, db: Session = Depends(get_db)):
    return FuncionarioService.create(db, data)


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
def update(id: int, data: FuncionarioUpdate, db: Session = Depends(get_db)):
    try:
        return FuncionarioService.update(db, id, data)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    try:
        return FuncionarioService.delete(db, id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc