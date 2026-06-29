from sqlalchemy import ( Boolean, Column, DateTime, Integer, Numeric, String,)
from sqlalchemy.sql import func

from backend.app.core.database import Base


class Funcionario(Base):
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String(100), nullable=False)
    cpf = Column(String(14), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)

    cargo = Column(String(50), nullable=False)
    telefone = Column(String(20), nullable=False)

    salario = Column(Numeric(10, 2), nullable=True)
    especialidade = Column(String(100), nullable=True)
    nivel_experiencia = Column(Integer, default=1)
    comissao_percentual = Column(Numeric(5, 2), default=0)

    ativo = Column(Boolean, default=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )