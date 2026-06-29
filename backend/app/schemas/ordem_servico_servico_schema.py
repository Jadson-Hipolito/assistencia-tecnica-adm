from typing import Optional

from pydantic import BaseModel, ConfigDict


class OrdemServicoServicoBase(BaseModel):
    ordem_servico_id: int
    servico_id: int
    quantidade: int
    valor_aplicado: float


class OrdemServicoServicoCreate(OrdemServicoServicoBase):
    pass


class OrdemServicoServicoResponse(OrdemServicoServicoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)