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

        documento = payload.pop("documento", None)
        contato = payload.pop("contato", None)

        cliente = Cliente(
            nome=payload.get("nome"),
            cpf=documento,
            telefone=contato,
            endereco=payload.get("endereco"),
            email=payload.get("email", None),
            cnpj=None,
            ativo=payload.get("ativo", True),
        )

        cliente = self._commit_and_refresh(cliente)

        # 🔥 IMPORTANTE: normalizar resposta para API
        cliente.documento = cliente.cpf
        cliente.contato = cliente.telefone

        return cliente

    def list_all(self) -> list[Cliente]:
        clientes = self.repository.get_all()

        # normaliza para API
        for c in clientes:
            c.documento = c.cpf
            c.contato = c.telefone

        return clientes

    def get_by_id(self, cliente_id: int) -> Cliente:
        cliente = self.repository.get_by_id(cliente_id)
        if not cliente:
            raise ValueError("Cliente não encontrado")

        cliente.documento = cliente.cpf
        cliente.contato = cliente.telefone
        return cliente

    def update(self, cliente_id: int, data) -> Cliente:
        cliente = self.get_by_id(cliente_id)

        for field, value in self._to_dict(data).items():
            if field in {"id", "created_at", "updated_at"}:
                continue
            setattr(cliente, field, value)

        cliente = self.repository.update(cliente)

        cliente.documento = cliente.cpf
        cliente.contato = cliente.telefone

        return cliente

    def delete(self, cliente_id: int) -> Cliente:
        cliente = self.get_by_id(cliente_id)
        cliente.ativo = False

        cliente = self.repository.update(cliente)

        cliente.documento = cliente.cpf
        cliente.contato = cliente.telefone

        return cliente

    @staticmethod
    def criar_cliente(db: Session, data):
        return ClienteService(db).create(data)

    @staticmethod
    def listar(db: Session):
        return ClienteService(db).list_all()

    @staticmethod
    def desativar(db: Session, cliente_id: int):
        return ClienteService(db).delete(cliente_id)