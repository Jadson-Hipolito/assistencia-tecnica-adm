from pydantic import BaseModel, Field


class PagamentoCreate(BaseModel):
    ordem_servico_id: int
    valor: float = Field(..., gt=0)
    forma_pagamento: str
    status: str

class PagamentoUpdate(BaseModel):

    valor: float | None = None

    forma_pagamento: str | None = None

    status: str | None = None


class PagamentoResponse(BaseModel):
    id: int
    ordem_servico_id: int
    valor: float
    forma_pagamento: str
    status: str