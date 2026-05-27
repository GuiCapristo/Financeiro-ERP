from sqlalchemy import Column, String, Float, Date, Enum as SQLEnum
from sqlalchemy.dialects.sqlite import CHAR
from uuid import uuid4
from app.core.database import Base
from enum import Enum


class TipoTransacao(str, Enum):
    entrada = "entrada"
    saida = "saida"


class StatusTransacao(str, Enum):
    pendente = "pendente"
    pago = "pago"


class Transacao(Base):
    __tablename__ = "transacoes"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid4()))
    descricao = Column(String(100), nullable=False)
    valor = Column(Float, nullable=False)
    tipo = Column(SQLEnum(TipoTransacao), nullable=False)
    status = Column(SQLEnum(StatusTransacao), default=StatusTransacao.pendente)
    data_vencimento = Column(Date, nullable=False)
