from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.core.dependencies import get_db
from backend.app.schemas.aparelho_schema import AparelhoCreate, AparelhoResponse, AparelhoUpdate
from backend.app.services.aparelho_service import AparelhoService

router = APIRouter(prefix="/aparelhos", tags=["Aparelhos"])


@router.post("/", response_model=AparelhoResponse, status_code=201)
def create(data: AparelhoCreate, db: Session = Depends(get_db)):
    try:
        return AparelhoService(db).criar(data)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get("/", response_model=list[AparelhoResponse])
def list_all(db: Session = Depends(get_db)):
    return AparelhoService(db).listar_todos()


@router.get("/{id}", response_model=AparelhoResponse)
def get(id: int, db: Session = Depends(get_db)):
    try:
        return AparelhoService(db).get_by_id(id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.put("/{id}", response_model=AparelhoResponse)
def update(id: int, data: AparelhoUpdate, db: Session = Depends(get_db)):
    try:
        return AparelhoService(db).update(id, data)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
