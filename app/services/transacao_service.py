from uuid import UUID
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories import transacao_repository as repo
from app.models.transacao import Transacao as TransacaoModel
from app.schemas.transacao_schema import TransacaoCreate


def criar_transacao(db: Session, transacao: TransacaoCreate):
    db_transacao = TransacaoModel(
        id=str(transacao.id),
        descricao=transacao.descricao,
        valor=transacao.valor,
        tipo=transacao.tipo.value,
        status=transacao.status.value,
        data_vencimento=transacao.data_vencimento
    )
    repo.salvar(db, db_transacao)
    return {"msg": "Transação criada com sucesso", "id": str(db_transacao.id)}


def listar_transacoes(db: Session):
    transacoes = repo.listar(db)
    return [
        {
            "id": t.id,
            "descricao": t.descricao,
            "valor": t.valor,
            "tipo": t.tipo,
            "status": t.status,
            "data_vencimento": str(t.data_vencimento)
        }
        for t in transacoes
    ]


def buscar_transacao_por_id(db: Session, transacao_id: UUID):
    transacao = repo.buscar_por_id(db, transacao_id)
    if not transacao:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    return {
        "id": transacao.id,
        "descricao": transacao.descricao,
        "valor": transacao.valor,
        "tipo": transacao.tipo,
        "status": transacao.status,
        "data_vencimento": str(transacao.data_vencimento)
    }


def calcular_fluxo_caixa(db: Session):
    entradas = 0
    saidas = 0
    for t in repo.listar(db):
        if t.tipo == "entrada":
            entradas += t.valor
        elif t.tipo == "saida":
            saidas += t.valor
    return {
        "total_entradas": entradas,
        "total_saidas": saidas,
        "saldo": entradas - saidas
    }


def pagar_conta(db: Session, transacao_id: UUID):
    transacao = repo.buscar_por_id(db, transacao_id)
    if not transacao:
        raise HTTPException(status_code=404, detail="Transação não encontrada")
    if transacao.status == "pago":
        return {"msg": "Conta já está paga"}
    atualizado = repo.atualizar(db, transacao_id, {"status": "pago"})
    return {
        "msg": "Conta marcada como paga",
        "transacao": {
            "id": atualizado.id,
            "descricao": atualizado.descricao,
            "valor": atualizado.valor,
            "tipo": atualizado.tipo,
            "status": atualizado.status,
            "data_vencimento": str(atualizado.data_vencimento)
        }
    }
