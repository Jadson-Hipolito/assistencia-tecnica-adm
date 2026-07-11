import hashlib

from sqlalchemy.orm import Session

from backend.app.models.funcionario import Funcionario
from backend.app.services.base_service import BaseService
from backend.app.services.auditoria_service import AuditoriaService


class FuncionarioService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db)

    @classmethod
    def create(cls, db: Session, data, executor_id: int) -> Funcionario:
        return cls(db).criar_funcionario(data, executor_id)

    @classmethod
    def list_all(cls, db: Session) -> list[Funcionario]:
        return cls(db).listar_funcionarios()

    @classmethod
    def get_by_id(cls, db: Session, funcionario_id: int) -> Funcionario:
        return cls(db).buscar_por_id(funcionario_id)

    @classmethod
    def update(cls, db: Session, funcionario_id: int, data, executor_id: int) -> Funcionario:
        service = cls(db)

        funcionario = service.buscar_por_id(funcionario_id)

        dados = data.model_dump(exclude_unset=True)

        for field, value in dados.items():
    
            if field in {"id", "cpf", "created_at", "updated_at"}:
                continue

            setattr(funcionario, field, value)

        service.db.commit()
        service.db.refresh(funcionario)
        AuditoriaService(service.db).registrar(
            funcionario_id=executor_id,
            acao="UPDATE",
            entidade="Funcionário"
        )
        return funcionario

    @classmethod
    def delete(cls, db: Session, funcionario_id: int, executor_id: int) -> Funcionario:
        return cls(db).desativar_funcionario(funcionario_id, executor_id)

    def criar_funcionario(self, data, executor_id: int) -> Funcionario:
        existente = self.db.query(Funcionario).filter(Funcionario.email == data.email).first()
        if existente:
            raise ValueError("Email já cadastrado")

        funcionario = Funcionario(
            nome=data.nome,
            cpf=data.cpf,
            email=data.email,
            senha=self._hash_senha(data.senha),
            cargo=data.cargo,
            telefone=data.telefone,
            salario=data.salario or 0,
            ativo=True,
        )

        funcionario = self._commit_and_refresh(funcionario)


        AuditoriaService(self.db).registrar(
            funcionario_id=executor_id,
            acao="CREATE",
            entidade="Funcionário"
        )

        return funcionario

    def listar_funcionarios(self) -> list[Funcionario]:
        return self.db.query(Funcionario).all()

    def buscar_por_id(self, funcionario_id: int) -> Funcionario:
        return self._get_or_raise(Funcionario, funcionario_id, "Funcionário não encontrado")

    def desativar_funcionario(self, funcionario_id: int, executor_id: int) -> Funcionario:
        funcionario = self.buscar_por_id(funcionario_id)
        funcionario.ativo = False
        self.db.commit()
        self.db.refresh(funcionario)
        AuditoriaService(self.db).registrar(
            funcionario_id=executor_id,
            acao="DELETE",
            entidade="Funcionário"
        )       
        return funcionario

    @staticmethod
    def _hash_senha(senha: str) -> str:
        return hashlib.sha256(senha.encode("utf-8")).hexdigest()
    