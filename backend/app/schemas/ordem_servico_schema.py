from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class OrdemServicoBase(BaseModel):
    descricao: str
    status: str
    cliente_id: int
    aparelho_id: int


class OrdemServicoCreate(OrdemServicoBase):
    pass


class OrdemServicoUpdate(BaseModel):
    descricao: Optional[str] = None
    status: Optional[str] = None


class OrdemServicoResponse(OrdemServicoBase):
    id: int
    data_abertura: datetime
    data_fechamento: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)