from typing import Optional

from pydantic import BaseModel, ConfigDict


class ClienteBase(BaseModel):
    nome: str
    documento: str  # CPF/CNPJ
    endereco: str
    contato: str
    ativo: bool = True


class ClienteCreate(ClienteBase):
    pass


class ClienteUpdate(BaseModel):
    nome: Optional[str] = None
    documento: Optional[str] = None
    endereco: Optional[str] = None
    contato: Optional[str] = None
    ativo: Optional[bool] = None


class ClienteResponse(BaseModel):
    id: int
    nome: str
    documento: str | None = None
    endereco: str
    contato: str | None = None
    ativo: bool = True

    model_config = ConfigDict(from_attributes=True)