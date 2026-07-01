from typing import Optional

from pydantic import BaseModel, ConfigDict


class AparelhoBase(BaseModel):
    tipo: str
    marca: str
    modelo: str
    numero_serie: str
    cliente_id: int


class AparelhoCreate(AparelhoBase):
    pass


class AparelhoUpdate(BaseModel):
    tipo: Optional[str] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    numero_serie: Optional[str] = None
    cliente_id: Optional[int] = None


class AparelhoResponse(AparelhoBase):
    id: int

    model_config = ConfigDict(from_attributes=True)