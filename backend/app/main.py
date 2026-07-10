from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.app.core.database import Base, engine
from backend.app.routers.api_router import api_router


def create_app() -> FastAPI:

    app = FastAPI(
        title="Sistema de Gestão de Assistência Técnica",
        description="API para gestão de assistência técnica",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


    # ==========================
    # ROTAS DA API
    # ==========================

    app.include_router(api_router)


    # ==========================
    # FRONTEND
    # ==========================

    app.mount(
        "/",
        StaticFiles(
            directory="frontend",
            html=True
        ),
        name="frontend"
    )


    return app


app = create_app()


Base.metadata.create_all(bind=engine)