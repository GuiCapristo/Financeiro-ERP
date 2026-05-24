from pydantic import BaseModel
from uuid import UUID, uuid4

class Transacao(BaseModel):
    id: UUID = uuid4()
    tipo: str  # entrada ou saida
    valor: float
    descricao: str
    status: str = "pendente"