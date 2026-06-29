from sqlalchemy import Boolean, Column, DateTime, Integer, Numeric, String
from sqlalchemy.sql import func

from backend.app.core.database import Base


class Servico(Base):
    __tablename__ = "servicos"

    # =========================
    # Identificação
    # =========================
    id = Column(Integer, primary_key=True, index=True)

    # =========================
    # Dados do serviço
    # =========================
    nome = Column(String(150), nullable=False, unique=True, index=True)

    descricao = Column(String(255), nullable=True)

    valor_padrao = Column(Numeric(10, 2), nullable=False)

    # =========================
    # Status
    # =========================
    ativo = Column(Boolean, default=True, nullable=False)

    # =========================
    # Auditoria
    # =========================
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )