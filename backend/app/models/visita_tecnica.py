from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.app.core.database import Base


class VisitaTecnica(Base):
    __tablename__ = "visitas_tecnicas"

    # =========================
    # Identificação
    # =========================
    id = Column(Integer, primary_key=True, index=True)

    # =========================
    # Relacionamentos
    # =========================
    ordem_servico_id = Column(
        Integer,
        ForeignKey("ordens_servico.id"),
        nullable=False
    )

    funcionario_id = Column(
        Integer,
        ForeignKey("funcionarios.id"),
        nullable=True
    )

    # =========================
    # Dados da visita
    # =========================
    data_agendamento = Column(DateTime, nullable=False)

    data_realizacao = Column(DateTime, nullable=True)

    status = Column(String(30), default="AGENDADA")

    resultado = Column(String(255), nullable=True)

    # =========================
    # Auditoria simples (opcional mas recomendado)
    # =========================
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # =========================
    # Relationships
    # =========================
    ordem_servico = relationship("OrdemServico", backref="visitas_tecnicas")
    funcionario = relationship("Funcionario", backref="visitas_tecnicas")