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

    def calcular_comissao(self, valor: float) -> float:
        return float((valor * self.comissao_percentual) / 100)

    def __init__(
        self,
        nome: str,
        email: str,
        cargo: str,
        telefone: str,
        salario: float,
        cpf: str,
        senha: str,
        nivel_experiencia: int = 1,
        comissao_percentual: float = 0.0,
        especialidade: str | None = None,
        ativo: bool = True,
    ):
        if nivel_experiencia < 1 or nivel_experiencia > 5:
            raise ValueError("Nível de experiência deve ser entre 1 e 5")
        if comissao_percentual < 0 or comissao_percentual > 30:
            raise ValueError("Comissão deve ser entre 0% e 30%")

        self.nome = nome
        self.email = email
        self.cargo = cargo
        self.telefone = telefone
        self.salario = salario
        self.cpf = cpf
        self.senha = senha
        self.nivel_experiencia = nivel_experiencia
        self.comissao_percentual = comissao_percentual
        self.especialidade = especialidade
        self.ativo = ativo
