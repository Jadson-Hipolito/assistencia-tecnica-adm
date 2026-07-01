from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.core.dependencies import get_db
from backend.app.schemas.visita_tecnica_schema import VisitaTecnicaCreate, VisitaTecnicaResponse, VisitaTecnicaUpdate
from backend.app.services.visita_tecnica_service import VisitaTecnicaService

router = APIRouter(prefix="/visitas-tecnicas", tags=["Visitas Técnicas"])


@router.post("/", response_model=VisitaTecnicaResponse, status_code=201)
def create(data: VisitaTecnicaCreate, db: Session = Depends(get_db)):
    try:
        return VisitaTecnicaService(db).agendar(data)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get("/", response_model=list[VisitaTecnicaResponse])
def list_all(db: Session = Depends(get_db)):
    return VisitaTecnicaService(db).listar_todas()


@router.get("/{id}", response_model=VisitaTecnicaResponse)
def get(id: int, db: Session = Depends(get_db)):
    try:
        return VisitaTecnicaService(db).get_by_id(id)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.put("/{id}", response_model=VisitaTecnicaResponse)
def update(id: int, data: VisitaTecnicaUpdate, db: Session = Depends(get_db)):
    try:
        return VisitaTecnicaService(db).update(id, data)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
