from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from backend.app.core.database import Base


class Equipamento(Base):
    __tablename__ = "equipamentos"

    # =========================
    # Identificação
    # =========================
    id = Column(Integer, primary_key=True, index=True)

    # =========================
    # Dados do equipamento
    # =========================
    nome = Column(String(150), nullable=False, index=True)

    tipo = Column(String(100), nullable=False)

    marca = Column(String(100), nullable=True)

    modelo = Column(String(100), nullable=True)

    codigo = Column(String(50), unique=True, nullable=False, index=True)

    descricao = Column(String(255), nullable=True)

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