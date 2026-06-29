import hashlib

from sqlalchemy.orm import Session

from backend.app.models.funcionario import Funcionario
from backend.app.services.base_service import BaseService


class FuncionarioService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db)

    @classmethod
    def create(cls, db: Session, data) -> Funcionario:
        return cls(db).criar_funcionario(data)

    @classmethod
    def list_all(cls, db: Session) -> list[Funcionario]:
        return cls(db).listar_funcionarios()

    @classmethod
    def get_by_id(cls, db: Session, funcionario_id: int) -> Funcionario:
        return cls(db).buscar_por_id(funcionario_id)

    @classmethod
    def update(cls, db: Session, funcionario_id: int, data) -> Funcionario:
        service = cls(db)
        funcionario = service.buscar_por_id(funcionario_id)
        for field, value in service._to_dict(data).items():
            if field in {"id", "created_at", "updated_at"}:
                continue
            setattr(funcionario, field, value)
        service.db.commit()
        service.db.refresh(funcionario)
        return funcionario

    @classmethod
    def delete(cls, db: Session, funcionario_id: int) -> Funcionario:
        return cls(db).desativar_funcionario(funcionario_id)

    def criar_funcionario(self, data) -> Funcionario:
        existente = self.db.query(Funcionario).filter(Funcionario.email == data.email).first()
        if existente:
            raise ValueError("Email já cadastrado")

        funcionario = Funcionario(
            nome=data.nome,
            email=data.email,
            senha=self._hash_senha(data.senha),
            cargo=getattr(data, "cargo", getattr(data, "perfil", "tecnico")),
            telefone=data.telefone,
            ativo=True,
        )

        return self._commit_and_refresh(funcionario)

    def listar_funcionarios(self) -> list[Funcionario]:
        return self.db.query(Funcionario).all()

    def buscar_por_id(self, funcionario_id: int) -> Funcionario:
        return self._get_or_raise(Funcionario, funcionario_id, "Funcionário não encontrado")

    def desativar_funcionario(self, funcionario_id: int) -> Funcionario:
        funcionario = self.buscar_por_id(funcionario_id)
        funcionario.ativo = False
        self.db.commit()
        self.db.refresh(funcionario)
        return funcionario

    @staticmethod
    def _hash_senha(senha: str) -> str:
        return hashlib.sha256(senha.encode("utf-8")).hexdigest()
    