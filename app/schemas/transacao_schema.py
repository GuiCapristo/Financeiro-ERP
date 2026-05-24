from pydantic import BaseModel, Field, field_validator
from datetime import date
from enum import Enum
from uuid import UUID, uuid4

class TipoTransacao(str, Enum):
    entrada = "entrada"
    saida = "saida"

class StatusTransacao(str, Enum):
    pendente = "pendente"
    pago = "pago"

class Transacao(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    descricao: str = Field(min_length=3, max_length=100)
    valor: float = Field(gt=0, le=1000000)
    tipo: TipoTransacao
    status: StatusTransacao
    data_vencimento: date

    model_config = {
        "extra": "forbid"
    }

    @field_validator("descricao")
    def limpar_texto(cls, v):
        return v.strip().title()

class ContaPagar(BaseModel):
    descricao: str = Field(min_length=3, max_length=100)
    valor: float = Field(gt=0, le=1000000)
    status: StatusTransacao
    data_vencimento: date

    model_config = {
        "extra": "forbid"
    }

    @field_validator("descricao")
    def limpar_texto(cls, v):
        return v.strip().title()

class ContaReceber(BaseModel):
    descricao: str = Field(min_length=3, max_length=100)
    valor: float = Field(gt=0, le=1000000)
    status: StatusTransacao
    data_vencimento: date

    model_config = {
        "extra": "forbid"
    }

    @field_validator("descricao")
    def limpar_texto(cls, v):
        return v.strip().title()