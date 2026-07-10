from backend.app.core.security import create_access_token, hash_password, verify_password
from backend.app.models.cliente import Cliente
from backend.app.models.funcionario import Funcionario

ADMIN_EMAIL = "admin@assistencia.com"
ADMIN_PASSWORD = "admin123"


class AuthService:
    @staticmethod
    def login(db, email: str, senha: str):
        funcionario = (
            db.query(Funcionario)
            .filter(Funcionario.email == email)
            .first()
        )

        if funcionario and funcionario.ativo and verify_password(senha, funcionario.senha):
            perfil = "admin" if funcionario.cargo.lower() == "admin" else "tecnico"

            payload = {
                "sub": str(funcionario.id),
                "email": funcionario.email,
                "role": perfil,
                "name": funcionario.nome,
            }

            return create_access_token(payload)

        cliente = (
            db.query(Cliente)
            .filter(Cliente.email == email)
            .first()
        )

        if cliente and cliente.ativo and senha == "123456":
            payload = {
                "sub": str(cliente.id),
                "email": cliente.email,
                "role": "cliente",
                "name": cliente.nome,
            }

            return create_access_token(payload)

        if email == ADMIN_EMAIL and senha == ADMIN_PASSWORD:
            payload = {
                "sub": "0",
                "email": ADMIN_EMAIL,
                "role": "admin",
                "name": "Admin",
            }

            return create_access_token(payload)

        return None

    @staticmethod
    def create_admin_if_missing(db):
        admin = (
            db.query(Funcionario)
            .filter(Funcionario.email == ADMIN_EMAIL)
            .first()
        )

        if not admin:
            admin = Funcionario(
                nome="Admin",
                cpf="00000000000",
                email=ADMIN_EMAIL,
                senha=hash_password(ADMIN_PASSWORD),
                cargo="admin",
                telefone="00000000000",
                salario=0,
                ativo=True,
            )

            db.add(admin)
            db.commit()
            db.refresh(admin)

        return admin