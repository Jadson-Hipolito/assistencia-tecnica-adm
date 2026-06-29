from sqlalchemy.orm import Session

from backend.app.models.aparelho import Aparelho
from backend.app.services.base_service import BaseService


class AparelhoService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db)

    def criar(self, data) -> Aparelho:
        aparelho = Aparelho(**self._to_dict(data))
        return self._commit_and_refresh(aparelho)

    def listar_por_cliente(self, cliente_id: int) -> list[Aparelho]:
        return self.db.query(Aparelho).filter(Aparelho.cliente_id == cliente_id).all()