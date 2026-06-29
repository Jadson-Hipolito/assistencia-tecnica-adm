from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.core.database import Base, engine
from backend.app.models import (
    funcionario,
    cliente,
    servico,
    equipamento,
    aparelho,
    ordem_servico,
    ordem_servico_servico,
    visita_tecnica,
    conta_receber,
    auditoria_log,
)
from backend.app.routers.auth_router import router as auth_router
from backend.app.routers.funcionario_router import router as funcionario_router
from backend.app.routers.cliente_router import router as cliente_router
from backend.app.routers.ordem_servico_router import router as ordem_servico_router
from backend.app.routers.servico_router import router as servico_router
from backend.app.routers.pagamento_router import router as pagamento_router
from backend.app.routers.auditoria_router import router as auditoria_router
from backend.app.routers.backup_router import router as backup_router
from backend.app.routers.api_router import api_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Sistema de Gestão de Assistência Técnica",
        description="API para gestão de assistência técnica",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(auth_router)
    app.include_router(funcionario_router)
    app.include_router(cliente_router)
    app.include_router(ordem_servico_router)
    app.include_router(servico_router)
    app.include_router(pagamento_router)
    app.include_router(auditoria_router)
    app.include_router(backup_router)
    app.include_router(api_router)

    @app.get("/")
    def root():
        return {"message": "Bem-vindo ao Sistema de Gestão de Assistência Técnica"}

    @app.get("/health")
    def health():
        return {"status": "ok", "message": "API está funcionando!"}

    return app


app = create_app()
Base.metadata.create_all(bind=engine)