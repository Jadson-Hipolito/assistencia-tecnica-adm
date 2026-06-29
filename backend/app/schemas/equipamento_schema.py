from typing import Optional

from pydantic import BaseModel, ConfigDict


class EquipamentoBase(BaseModel):
    nome: str
    tipo: str
    marca: str
    modelo: str
    ativo: bool = True


class EquipamentoCreate(EquipamentoBase):
    pass


class EquipamentoUpdate(BaseModel):
    nome: Optional[str] = None
    tipo: Optional[str] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    ativo: Optional[bool] = None


class EquipamentoResponse(EquipamentoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)