from sqlalchemy.orm import Session

from backend.app.core.security import hash_password
from backend.app.models.usuario import Usuario
from backend.app.services.base_service import BaseService


class UsuarioService(BaseService):
    def __init__(self, db: Session):
        super().__init__(db)

    def criar(self, data) -> Usuario:
        existente = self.db.query(Usuario).filter(Usuario.email == data.email).first()
        if existente:
            raise ValueError("Email já cadastrado")

        usuario = Usuario(
            nome=data.nome,
            email=data.email,
            senha=hash_password(data.senha),
            tipo=data.tipo,
            status="ATIVO",
        )
        return self._commit_and_refresh(usuario)

    def listar(self) -> list[Usuario]:
        return self.db.query(Usuario).all()

    def get_by_id(self, usuario_id: int) -> Usuario:
        return self._get_or_raise(Usuario, usuario_id, "Usuário não encontrado")

    def atualizar(self, usuario_id: int, data) -> Usuario:
        usuario = self.get_by_id(usuario_id)
        payload = self._to_dict(data)

        for field, value in payload.items():
            if field in {"id", "created_at", "updated_at"} or value is None:
                continue
            if field == "senha":
                value = hash_password(value)
            setattr(usuario, field, value)

        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def deletar(self, usuario_id: int) -> Usuario:
        usuario = self.get_by_id(usuario_id)
        self.db.delete(usuario)
        self.db.commit()
        return usuario
