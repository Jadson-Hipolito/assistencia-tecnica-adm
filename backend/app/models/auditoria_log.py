from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.app.core.database import Base


class AuditoriaLog(Base):
    __tablename__ = "auditoria_logs"

    # =========================
    # Identificação
    # =========================
    id = Column(Integer, primary_key=True, index=True)

    # =========================
    # Relacionamento
    # =========================
    funcionario_id = Column(
        Integer,
        ForeignKey("funcionarios.id"),
        nullable=True
    )

    # =========================
    # Dados da auditoria
    # =========================
    acao = Column(String(255), nullable=False)

    entidade = Column(String(100), nullable=True)

    data_hora = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    # =========================
    # Relationship ORM
    # =========================
    funcionario = relationship(
        "Funcionario",
        backref="auditorias"
    )