from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ContaReceberBase(BaseModel):
    ordem_servico_id: int
    valor_total: float
    data_vencimento: date
    status: str = "PENDENTE"


class ContaReceberCreate(ContaReceberBase):
    pass


class ContaReceberUpdate(BaseModel):
    ordem_servico_id: Optional[int] = None
    valor_total: Optional[float] = None
    data_vencimento: Optional[date] = None
    status: Optional[str] = None
    data_pagamento: Optional[datetime] = None


class ContaReceberResponse(ContaReceberBase):
    id: int
    data_emissao: datetime
    data_pagamento: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)