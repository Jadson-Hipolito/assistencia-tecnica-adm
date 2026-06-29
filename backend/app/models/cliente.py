from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func

from backend.app.core.database import Base


class Cliente(Base):
    __tablename__ = "clientes"

    # =========================
    # Identificação
    # =========================
    id = Column(Integer, primary_key=True, index=True)

    # =========================
    # Dados básicos
    # =========================
    nome = Column(String(150), nullable=False)

    email = Column(String(150), nullable=True)

    telefone = Column(String(20), nullable=False)

    endereco = Column(String(255), nullable=False)

    # =========================
    # Documento (PF ou PJ)
    # =========================
    cpf = Column(String(14), unique=True, nullable=True, index=True)

    cnpj = Column(String(18), unique=True, nullable=True, index=True)

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