from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.app.core.database import Base


class OrdemServico(Base):
    __tablename__ = "ordens_servico"

    # =========================
    # Identificação
    # =========================
    id = Column(Integer, primary_key=True, index=True)

    # =========================
    # Dados da OS
    # =========================
    status = Column(String(30), nullable=False, default="ABERTA")

    descricao = Column(String(255), nullable=False)

    data_abertura = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    data_fechamento = Column(DateTime(timezone=True), nullable=True)

    valor_total = Column(Numeric(10, 2), default=0)

    # =========================
    # Relacionamentos
    # =========================
    cliente_id = Column(
        Integer,
        ForeignKey("clientes.id"),
        nullable=False
    )

    aparelho_id = Column(
        Integer,
        ForeignKey("aparelhos.id"),
        nullable=False
    )

    funcionario_id = Column(
        Integer,
        ForeignKey("funcionarios.id"),
        nullable=True
    )

    # =========================
    # ORM relationships
    # =========================
    cliente = relationship("Cliente", backref="ordens_servico")
    aparelho = relationship("Aparelho", backref="ordens_servico")
    funcionario = relationship("Funcionario", backref="ordens_servico")