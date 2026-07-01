from .auth_router import router as auth_router
from .funcionario_router import router as funcionario_router
from .cliente_router import router as cliente_router
from .ordem_servico_router import router as ordem_servico_router
from .servico_router import router as servico_router
from .pagamento_router import router as pagamento_router
from .auditoria_router import router as auditoria_router
from .backup_router import router as backup_router
from .conta_receber_router import router as conta_receber_router
from .aparelho_router import router as aparelho_router
from .equipamento_router import router as equipamento_router
from .visita_tecnica_router import router as visita_tecnica_router
from .usuario_router import router as usuario_router
from .relatorio_router import router as relatorio_router

__all__ = [
    "auth_router",
    "funcionario_router",
    "cliente_router",
    "ordem_servico_router",
    "servico_router",
    "pagamento_router",
    "auditoria_router",
    "backup_router",
    "conta_receber_router",
    "aparelho_router",
    "equipamento_router",
    "visita_tecnica_router",
]
