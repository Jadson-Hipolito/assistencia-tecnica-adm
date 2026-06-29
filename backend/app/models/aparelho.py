from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.app.core.database import Base


class Aparelho(Base):
    __tablename__ = "aparelhos"

    # =========================
    # Identificação
    # =========================
    id = Column(Integer, primary_key=True, index=True)

    # =========================
    # Dados do aparelho
    # =========================
    tipo = Column(String(100), nullable=False)

    marca = Column(String(100), nullable=False)

    modelo = Column(String(100), nullable=False)

    numero_serie = Column(String(100), unique=True, nullable=False, index=True)

    cor = Column(String(50), nullable=True)

    observacoes = Column(String(255), nullable=True)

    # =========================
    # Relacionamento
    # =========================
    cliente_id = Column(
        Integer,
        ForeignKey("clientes.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

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

    # =========================
    # Relationship (SQLAlchemy ORM)
    # =========================
    cliente = relationship("Cliente", backref="aparelhos")