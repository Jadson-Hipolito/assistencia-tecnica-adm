from pydantic import BaseModel, Field
from typing import Optional


class PagamentoCreate(BaseModel):
    ordem_servico_id: int
    valor: float = Field(..., gt=0)
    forma_pagamento: Optional[str] = "PIX"


class PagamentoResponse(BaseModel):
    id: int
    ordem_servico_id: int
    valor: float
    forma_pagamento: str