from dataclasses import dataclass
from typing import Literal
from pydantic import BaseModel, Field


@dataclass
class GastoSimple:
    descripcion: str
    monto: float


class Gasto(BaseModel):
    descripcion: str = Field(min_length=3, description="Qué se gastó")
    monto: float = Field(gt=0, description="Cuánto se gastó")
    categoria: Literal["comida", "transporte", "entretenimiento", "otros"]
