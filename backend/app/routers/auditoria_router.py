from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.services.auditoria_service import AuditoriaService
from backend.app.core.dependencies import get_db

router = APIRouter(prefix="/auditoria", tags=["Auditoria"])

@router.get("/")
def list_logs(db: Session = Depends(get_db)):
    service = AuditoriaService(db)

    logs = service.listar()

    return [
        {
            "id": log.id,
            "usuario": log.funcionario.nome if log.funcionario else "sistema",
            "acao": log.acao,
            "entidade": log.entidade,
            "data": log.data_hora
        }
        for log in logs
    ]