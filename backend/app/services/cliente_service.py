from sqlalchemy.orm import Session

from backend.app.models.cliente import Cliente
from backend.app.repositories.cliente_repository import ClienteRepository
from backend.app.services.base_service import BaseService


class ClienteService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db)
        self.repository = ClienteRepository(db)

    def create(self, data) -> Cliente:
        payload = self._to_dict(data)
        document = payload.pop("documento", None)
        contact = payload.pop("contato", None)

        payload.setdefault("email", None)
        payload.setdefault("telefone", contact)
        payload.setdefault("cpf", document)
        payload.setdefault("cnpj", None)
        payload.setdefault("endereco", payload.get("endereco"))

        cliente = Cliente(**payload)
        return self._commit_and_refresh(cliente)

    def list_all(self) -> list[Cliente]:
        return self.repository.get_all()

    def get_by_id(self, cliente_id: int) -> Cliente:
        cliente = self.repository.get_by_id(cliente_id)
        if not cliente:
            raise ValueError("Cliente não encontrado")
        return cliente

    def update(self, cliente_id: int, data) -> Cliente:
        cliente = self.get_by_id(cliente_id)
        for field, value in self._to_dict(data).items():
            if field in {"id", "created_at", "updated_at"}:
                continue
            setattr(cliente, field, value)
        return self.repository.update(cliente)

    def delete(self, cliente_id: int) -> Cliente:
        cliente = self.get_by_id(cliente_id)
        cliente.ativo = False
        return self.repository.update(cliente)

    @staticmethod
    def criar_cliente(db: Session, data):
        return ClienteService(db).create(data)

    @staticmethod
    def listar(db: Session):
        return ClienteService(db).list_all()

    @staticmethod
    def desativar(db: Session, cliente_id: int):
        return ClienteService(db).delete(cliente_id)