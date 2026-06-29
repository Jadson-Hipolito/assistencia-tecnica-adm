from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class VisitaTecnicaBase(BaseModel):
    ordem_servico_id: int
    funcionario_id: Optional[int] = None
    data_agendamento: datetime
    resultado: Optional[str] = None
    status: str = "AGENDADA"


class VisitaTecnicaCreate(VisitaTecnicaBase):
    pass


class VisitaTecnicaUpdate(BaseModel):
    data_agendamento: Optional[datetime] = None
    data_realizacao: Optional[datetime] = None
    resultado: Optional[str] = None
    status: Optional[str] = None


class VisitaTecnicaResponse(VisitaTecnicaBase):
    id: int
    data_realizacao: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)