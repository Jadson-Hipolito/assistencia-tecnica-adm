from sqlalchemy.orm import Session

from backend.app.models.servico import Servico
from backend.app.services.base_service import BaseService
from backend.app.services.auditoria_service import AuditoriaService


class ServicoService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db)

    def criar(self, data, executor_id: int) -> Servico:

        existente = (
            self.db.query(Servico)
            .filter(Servico.nome == data.nome)
            .first()
        )

        if existente:
            raise ValueError("Serviço já cadastrado")

        servico = Servico(**self._to_dict(data))

        servico = self._commit_and_refresh(servico)

        AuditoriaService(self.db).registrar(
            funcionario_id=executor_id,
            acao="CREATE",
            entidade="Servico"
        )

        return servico

    def listar(self) -> list[Servico]:
        return (
            self.db.query(Servico)
            .filter(Servico.ativo == True)
            .all()
        )

    def desativar(
        self,
        servico_id: int,
        executor_id: int
    ) -> Servico:

        servico = self._get_or_raise(
            Servico,
            servico_id,
            "Serviço não encontrado"
        )

        servico.ativo = False

        self.db.commit()
        self.db.refresh(servico)

        AuditoriaService(self.db).registrar(
            funcionario_id=executor_id,
            acao="DELETE",
            entidade="Servico"
        )

        return servico