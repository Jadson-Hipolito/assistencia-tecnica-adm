from sqlalchemy.orm import Session

from backend.app.models.equipamento import Equipamento
from backend.app.services.base_service import BaseService


class EquipamentoService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db)

    def criar(self, data) -> Equipamento:
        equipamento = Equipamento(**self._to_dict(data))
        return self._commit_and_refresh(equipamento)

    def get_by_id(self, equipamento_id: int) -> Equipamento:
        return self._get_or_raise(Equipamento, equipamento_id, "Equipamento não encontrado")

    def update(self, equipamento_id: int, data) -> Equipamento:
        equipamento = self.get_by_id(equipamento_id)
        payload = self._to_dict(data)
        for field, value in payload.items():
            if field in {"id", "created_at", "updated_at"} or value is None:
                continue
            setattr(equipamento, field, value)
        self.db.commit()
        self.db.refresh(equipamento)
        return equipamento

    def listar_todos(self) -> list[Equipamento]:
        return self.db.query(Equipamento).all()

    def desativar(self, equipamento_id: int) -> Equipamento:
        equipamento = self._get_or_raise(Equipamento, equipamento_id, "Equipamento não encontrado")
        equipamento.ativo = False
        self.db.commit()
        self.db.refresh(equipamento)
        return equipamento