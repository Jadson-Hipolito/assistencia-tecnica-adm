from pydantic import BaseModel, Field


class PagamentoCreate(BaseModel):
    ordem_servico_id: int
    valor: float = Field(..., gt=0)
    forma_pagamento: str
    status: str


class PagamentoResponse(BaseModel):
    id: int
    ordem_servico_id: int
    valor: float
    forma_pagamento: str
    status: str