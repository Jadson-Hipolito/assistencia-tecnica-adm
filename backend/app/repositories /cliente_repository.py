from sqlalchemy.orm import Session

from backend.app.models.cliente import Cliente
from .base_repository import BaseRepository


class ClienteRepository(BaseRepository[Cliente]):
    def __init__(self, db: Session):
        super().__init__(Cliente, db)

    def get_by_email(self, email: str) -> Cliente | None:
        return self.db.query(Cliente).filter(Cliente.email == email).first()

    def get_active(self) -> list[Cliente]:
        return self.db.query(Cliente).filter(Cliente.ativo.is_(True)).all()