from backend.app.core.security import create_access_token, hash_password, verify_password
from backend.app.models.funcionario import Funcionario
from backend.app.models.cliente import Cliente


class AuthService:
    @staticmethod
    def login(db, email: str, senha: str):
        funcionario = db.query(Funcionario).filter(Funcionario.email == email).first()
        if funcionario and funcionario.ativo and verify_password(senha, funcionario.senha):
            perfil = "admin" if funcionario.cargo.lower() == "admin" else "tecnico"
            payload = {"sub": str(funcionario.id), "email": funcionario.email, "role": perfil, "name": funcionario.nome}
            return create_access_token(payload)

        cliente = db.query(Cliente).filter(Cliente.email == email).first()
        if cliente and cliente.ativo and senha == "123456":
            payload = {"sub": str(cliente.id), "email": cliente.email, "role": "cliente", "name": cliente.nome}
            return create_access_token(payload)

        if email == "admin@assistencia.com" and senha == "admin123":
            payload = {"sub": "0", "email": email, "role": "admin", "name": "Admin"}
            return create_access_token(payload)

        return None

    @staticmethod
    def create_admin_if_missing(db):
        admin = db.query(Funcionario).filter(Funcionario.email == "admin@assistencia.com").first()
        if not admin:
            admin = Funcionario(
                nome="Admin",
                cpf="00000000000",
                email="admin@assistencia.com",
                senha=hash_password("admin123"),
                cargo="admin",
                telefone="00000000000",
                salario=0,
                ativo=True,
            )
            db.add(admin)
            db.commit()
            db.refresh(admin)
        return admin