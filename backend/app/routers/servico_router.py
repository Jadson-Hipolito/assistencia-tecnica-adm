from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.schemas.servico_schema import ServicoCreate
from backend.app.services.servico_service import ServicoService
from backend.app.core.dependencies import get_db

router = APIRouter(prefix="/servicos", tags=["Serviços"])

@router.post("/")
def create(data: ServicoCreate, db: Session = Depends(get_db)):
    return ServicoService.create(db, data)

@router.get("/")
def list_all(db: Session = Depends(get_db)):
    return ServicoService.list_all(db)