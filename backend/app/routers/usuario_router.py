from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.core.dependencies import get_db
from backend.app.schemas.usuario_schema import UsuarioCreate, UsuarioResponse, UsuarioUpdate
from backend.app.services.usuario_service import UsuarioService

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


@router.post("/", response_model=UsuarioResponse, status_code=201)
def create(data: UsuarioCreate, db: Session = Depends(get_db)):
    try:
        return UsuarioService(db).criar(data)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get("/", response_model=list[UsuarioResponse])
def list_all(db: Session = Depends(get_db)):
    return UsuarioService(db).listar()


@router.get("/{id}", response_model=UsuarioResponse)
def get(id: int, db: Session = Depends(get_db)):
    try:
        return UsuarioService(db).get_by_id(id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.put("/{id}", response_model=UsuarioResponse)
def update(id: int, data: UsuarioUpdate, db: Session = Depends(get_db)):
    try:
        return UsuarioService(db).atualizar(id, data)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.delete("/{id}", response_model=UsuarioResponse)
def delete(id: int, db: Session = Depends(get_db)):
    try:
        return UsuarioService(db).deletar(id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
