from sqlalchemy import Column, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship

from backend.app.core.database import Base


class OrdemServicoServico(Base):
    __tablename__ = "ordem_servico_servicos"

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

    servico_id = Column(
        Integer,
        ForeignKey("servicos.id"),
        nullable=False
    )

    # =========================
    # Dados da execução
    # =========================
    quantidade = Column(Integer, default=1, nullable=False)

    valor_aplicado = Column(Numeric(10, 2), nullable=False)

    # =========================
    # ORM relationships
    # =========================
    ordem_servico = relationship("OrdemServico")
    servico = relationship("Servico")