from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.core.dependencies import get_db
from backend.app.core.dependencies_auth import get_current_user, require_roles
from backend.app.schemas.auth_schema import LoginSchema, UsuarioLogadoSchema
from backend.app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    AuthService.create_admin_if_missing(db)
    token = AuthService.login(db, data.email, data.senha)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
    return {
        "access_token": token,
        "token_type": "bearer",
        "token": token,
        "user": {"email": data.email},
    }


@router.get("/me", response_model=UsuarioLogadoSchema)
def me(payload: dict = Depends(get_current_user)):
    return {
        "id": int(payload.get("sub", 0)),
        "nome": payload.get("name", "Usuário"),
        "email": payload.get("email", ""),
        "perfil": payload.get("role", "cliente"),
    }


@router.get("/admin-only")
def admin_only(payload: dict = Depends(require_roles("admin"))):
    return {"message": "Acesso liberado", "user": payload}


@router.get("/tech-only")
def tech_only(payload: dict = Depends(require_roles("admin", "tecnico"))):
    return {"message": "Acesso liberado", "user": payload}


@router.post("/recuperar-senha")
def recuperar_senha(data: dict, db: Session = Depends(get_db)):
    return {"message": "Se o e-mail existir, enviaremos instruções."}


@router.post("/logout")
def logout():
    return {"message": "Logout realizado com sucesso."}