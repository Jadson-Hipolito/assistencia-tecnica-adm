from fastapi import APIRouter

from backend.app.routers import (
    auditoria_router,
    auth_router,
    backup_router,
    cliente_router,
    conta_receber_router,
    funcionario_router,
    ordem_servico_router,
    pagamento_router,
    servico_router,
)

api_router = APIRouter(prefix="/api")

api_router.include_router(auth_router)
api_router.include_router(funcionario_router)
api_router.include_router(cliente_router)
api_router.include_router(ordem_servico_router)
api_router.include_router(servico_router)
api_router.include_router(conta_receber_router)
api_router.include_router(pagamento_router)
api_router.include_router(auditoria_router)
api_router.include_router(backup_router)