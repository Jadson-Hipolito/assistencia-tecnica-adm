from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class AuditoriaLogBase(BaseModel):
    funcionario_id: Optional[int]
    acao: str
    entidade: str


class AuditoriaLogCreate(AuditoriaLogBase):
    pass


class AuditoriaLogResponse(AuditoriaLogBase):
    id: int
    data_hora: datetime

    model_config = ConfigDict(from_attributes=True)