from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.core.dependencies import get_db
from backend.app.models.cliente import Cliente
from backend.app.models.funcionario import Funcionario
from backend.app.models.usuario import Usuario

router = APIRouter(prefix="/relatorios", tags=["Relatórios"])


@router.get("/dashboard/resumo")
def dashboard_resumo(db: Session = Depends(get_db)):
    total_clientes = db.query(Cliente).count()
    total_usuarios = db.query(Usuario).count()
    total_funcionarios = db.query(Funcionario).count()

    return {
        "resumo": {
            "total_clientes": total_clientes,
            "total_usuarios": total_usuarios,
            "total_funcionarios": total_funcionarios,
        },
        "gerado_em": datetime.now().isoformat(),
    }


@router.get("/usuarios")
def relatorio_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return {
        "tipo": "usuarios",
        "usuarios": [
            {
                "id": usuario.id,
                "nome": usuario.nome,
                "email": usuario.email,
                "tipo": usuario.tipo,
                "status": usuario.status,
            }
            for usuario in usuarios
        ],
        "total": len(usuarios),
        "gerado_em": datetime.now().isoformat(),
    }


@router.get("/clientes")
def relatorio_clientes(db: Session = Depends(get_db)):
    clientes = db.query(Cliente).all()
    return {
        "tipo": "clientes",
        "clientes": [
            {
                "id": cliente.id,
                "nome": cliente.nome,
                "email": cliente.email,
                "telefone": cliente.telefone,
                "cpf": cliente.cpf,
                "cnpj": cliente.cnpj,
                "ativo": cliente.ativo,
            }
            for cliente in clientes
        ],
        "total": len(clientes),
        "gerado_em": datetime.now().isoformat(),
    }


@router.get("/funcionarios")
def relatorio_funcionarios(db: Session = Depends(get_db)):
    funcionarios = db.query(Funcionario).all()
    return {
        "tipo": "funcionarios",
        "funcionarios": [
            {
                "id": funcionario.id,
                "nome": funcionario.nome,
                "email": funcionario.email,
                "cargo": funcionario.cargo,
                "telefone": funcionario.telefone,
                "ativo": funcionario.ativo,
            }
            for funcionario in funcionarios
        ],
        "total": len(funcionarios),
        "gerado_em": datetime.now().isoformat(),
    }


@router.get("/completo")
def relatorio_completo(db: Session = Depends(get_db)):
    total_clientes = db.query(Cliente).count()
    total_usuarios = db.query(Usuario).count()
    total_funcionarios = db.query(Funcionario).count()

    return {
        "resumo_geral": {
            "total_geral": total_clientes + total_usuarios + total_funcionarios,
        },
        "gerado_em": datetime.now().isoformat(),
    }
