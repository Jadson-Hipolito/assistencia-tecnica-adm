from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class OrdemServicoServicoBase(BaseModel):
    ordem_servico_id: int = Field(alias="servico_executado_id")
    servico_id: int = Field(alias="equipamento_id")
    quantidade: int
    valor_aplicado: float = 0.0

    model_config = ConfigDict(populate_by_name=True, extra="ignore")


class OrdemServicoServicoCreate(OrdemServicoServicoBase):
    horas_utilizadas: Optional[float] = None
    observacoes: Optional[str] = None


class OrdemServicoServicoResponse(OrdemServicoServicoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)