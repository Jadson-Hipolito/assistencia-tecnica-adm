from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class OrdemServicoBase(BaseModel):
    descricao_problema: str
    status: str = "ABERTA"
    cliente_id: int
    aparelho_id: Optional[int] = None
    tecnico_id: Optional[int] = None
    valor_total: Optional[float] = 0.0


class OrdemServicoCreate(OrdemServicoBase):
    pass


class OrdemServicoUpdate(BaseModel):
    descricao_problema: Optional[str] = None
    status: Optional[str] = None
    tecnico_id: Optional[int] = None
    valor_total: Optional[float] = None


class OrdemServicoResponse(BaseModel):
    id: int
    descricao_problema: str
    status: str
    cliente_id: int
    aparelho_id: Optional[int] = None
    tecnico_id: Optional[int] = None
    valor_total: float
    data_abertura: datetime
    data_encerramento: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
