from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.schemas.pagamento_schema import PagamentoCreate
from backend.app.services.pagamento_service import PagamentoService
from backend.app.core.dependencies import get_db

router = APIRouter(prefix="/pagamentos", tags=["Pagamentos"])

@router.post("/")
def create(data: PagamentoCreate, db: Session = Depends(get_db)):
    return PagamentoService.create(db, data)

@router.get("/")
def list_all(db: Session = Depends(get_db)):
    return PagamentoService.list_all(db)