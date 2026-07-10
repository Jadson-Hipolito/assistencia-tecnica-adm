from fastapi import APIRouter

from backend.app.routers.auth_router import router as auth_router
from backend.app.routers.funcionario_router import router as funcionario_router
from backend.app.routers.cliente_router import router as cliente_router
from backend.app.routers.conta_receber_router import router as conta_receber_router
from backend.app.routers.ordem_servico_router import router as ordem_servico_router
from backend.app.routers.servico_router import router as servico_router
from backend.app.routers.pagamento_router import router as pagamento_router
from backend.app.routers.auditoria_router import router as auditoria_router
from backend.app.routers.backup_router import router as backup_router
from backend.app.routers.relatorio_router import router as relatorio_router
from backend.app.routers.usuario_router import router as usuario_router
from backend.app.routers.equipamento_router import router as equipamento_router

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
api_router.include_router(relatorio_router)
api_router.include_router(usuario_router)
api_router.include_router(equipamento_router)