from typing import List
from uuid import UUID

transacoes: List[dict] = []

def salvar(transacao: dict):
    transacoes.append(transacao)

def listar():
    return transacoes

def buscar_por_id(transacao_id: UUID):
    for t in transacoes:
        if str(t["id"]) == str(transacao_id):
            return t
    return None

def atualizar(transacao_id: UUID, novos_dados: dict):
    for i, t in enumerate(transacoes):
        if str(t["id"]) == str(transacao_id):
            transacoes[i].update(novos_dados)
            return transacoes[i]
    return None