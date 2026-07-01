from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from backend.app.core.database import Base
from backend.app.core.security import hash_password, verify_password
from backend.app.utils.validators import validar_senha


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)
    tipo = Column(String(50), nullable=True)
    status = Column(String(20), nullable=False, default="ATIVO")
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    @staticmethod
    def criptografar_senha(senha: str) -> str:
        return hash_password(senha)

    def autenticar(self, senha: str) -> bool:
        if self.senha and self.senha.startswith("pbkdf2_sha256$"):
            return verify_password(senha, self.senha)
        return self.senha == senha

    def alterar_senha(self, nova_senha: str) -> bool:
        if len(nova_senha) < 6:
            raise ValueError("Senha deve ter no mínimo 6 caracteres")
        self.senha = nova_senha
        return True

    def desativar(self):
        self.status = "INATIVO"
        return self

    def ativar(self):
        self.status = "ATIVO"
        return self
