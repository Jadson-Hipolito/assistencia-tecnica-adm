from typing import Optional

from pydantic import BaseModel, ConfigDict


class ServicoBase(BaseModel):
    nome: str
    descricao: str
    valor_padrao: float
    ativo: bool = True


class ServicoCreate(ServicoBase):
    pass


class ServicoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    valor_padrao: Optional[float] = None
    ativo: Optional[bool] = None


class ServicoResponse(ServicoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)