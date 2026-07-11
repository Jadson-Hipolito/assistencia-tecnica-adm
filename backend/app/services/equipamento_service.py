from sqlalchemy.orm import Session

from backend.app.models.equipamento import Equipamento
from backend.app.services.base_service import BaseService
from backend.app.services.auditoria_service import AuditoriaService


class EquipamentoService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db)

    def criar(self, data, funcionario_id: int) -> Equipamento:
        equipamento = Equipamento(**self._to_dict(data))

        equipamento = self._commit_and_refresh(equipamento)


        AuditoriaService(self.db).registrar(
            funcionario_id=funcionario_id,
            acao="CREATE",
            entidade="Equipamento"
        )


        return equipamento

    def get_by_id(self, equipamento_id: int) -> Equipamento:
        return self._get_or_raise(Equipamento, equipamento_id, "Equipamento não encontrado")

    def update(self, equipamento_id: int, data, funcionario_id: int) -> Equipamento:
        equipamento = self.get_by_id(equipamento_id)
        payload = self._to_dict(data)
        for field, value in payload.items():
            if field in {"id", "created_at", "updated_at"} or value is None:
                continue
            setattr(equipamento, field, value)
        self.db.commit()
        self.db.refresh(equipamento)
        AuditoriaService(self.db).registrar(
            funcionario_id=funcionario_id,
            acao="UPDATE",
            entidade="Equipamento"
        )
        return equipamento

    def listar_todos(self) -> list[Equipamento]:
        return self.db.query(Equipamento).all()

    def desativar(self, equipamento_id: int, funcionario_id: int) -> Equipamento:
        equipamento = self._get_or_raise(Equipamento, equipamento_id, "Equipamento não encontrado")
        equipamento.ativo = False
        self.db.commit()
        self.db.refresh(equipamento)
        AuditoriaService(self.db).registrar(
            funcionario_id=funcionario_id,
            acao="DELETE",
            entidade="Equipamento"
        )
        return equipamento