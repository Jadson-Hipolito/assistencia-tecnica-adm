from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from backend.app.core.database import Base


class ContaReceber(Base):
    __tablename__ = "contas_receber"

    # =========================
    # Identificação
    # =========================
    id = Column(Integer, primary_key=True, index=True)

    # =========================
    # Relacionamento
    # =========================
    ordem_servico_id = Column(
        Integer,
        ForeignKey("ordens_servico.id"),
        nullable=False
    )

    # =========================
    # Valores financeiros
    # =========================
    valor_total = Column(Numeric(10, 2), nullable=False)

    valor_multa = Column(Numeric(10, 2), default=0)

    valor_desconto = Column(Numeric(10, 2), default=0)

    # =========================
    # Datas
    # =========================
    data_emissao = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    data_vencimento = Column(Date, nullable=False)

    data_pagamento = Column(DateTime(timezone=True), nullable=True)

    # =========================
    # Status
    # =========================
    status = Column(String(20), default="PENDENTE")

    # =========================
    # Relationships
    # =========================
    ordem_servico = relationship(
        "OrdemServico",
        backref="contas_receber"
    )