from sqlalchemy.orm import Session

from backend.app.models.aparelho import Aparelho
from backend.app.services.base_service import BaseService


class AparelhoService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db)

    def criar(self, data) -> Aparelho:
        aparelho = Aparelho(**self._to_dict(data))
        return self._commit_and_refresh(aparelho)

    def get_by_id(self, aparelho_id: int) -> Aparelho:
        return self._get_or_raise(Aparelho, aparelho_id, "Aparelho não encontrado")

    def update(self, aparelho_id: int, data) -> Aparelho:
        aparelho = self.get_by_id(aparelho_id)
        payload = self._to_dict(data)
        for field, value in payload.items():
            if field in {"id", "created_at", "updated_at"} or value is None:
                continue
            setattr(aparelho, field, value)
        self.db.commit()
        self.db.refresh(aparelho)
        return aparelho

    def listar_por_cliente(self, cliente_id: int) -> list[Aparelho]:
        return self.db.query(Aparelho).filter(Aparelho.cliente_id == cliente_id).all()

    def listar_todos(self) -> list[Aparelho]:
        return self.db.query(Aparelho).all()