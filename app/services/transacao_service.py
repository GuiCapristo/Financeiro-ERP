from uuid import UUID
from fastapi import HTTPException
from app.repositories import transacao_repository as repo

def criar_transacao(transacao):
    repo.salvar(transacao.model_dump())
    return {"msg": "Transação criada com sucesso", "id": str(transacao.id)}

def listar_transacoes():
    return repo.listar()

def buscar_transacao_por_id(transacao_id: UUID):
    transacao = repo.buscar_por_id(transacao_id)
    if not transacao:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    return transacao

def calcular_fluxo_caixa():
    entradas = 0
    saidas = 0

    for t in repo.listar():
        if t["tipo"] == "entrada":
            entradas += t["valor"]
        elif t["tipo"] == "saida":
            saidas += t["valor"]

    return {
        "total_entradas": entradas,
        "total_saidas": saidas,
        "saldo": entradas - saidas
    }

def pagar_conta(transacao_id: UUID):
    transacao = repo.buscar_por_id(transacao_id)

    if not transacao:
        raise HTTPException(status_code=404, detail="Transação não encontrada")

    if transacao["status"] == "pago":
        return {"msg": "Conta já está paga"}

    atualizado = repo.atualizar(transacao_id, {"status": "pago"})

    return {"msg": "Conta marcada como paga", "transacao": atualizado}