from fastapi import APIRouter, HTTPException
from datetime import date
from uuid import UUID

from app.schemas.transacao_schema import (
    TransacaoCreate,
    ContaPagar,
    ContaReceber,
    TipoTransacao
)

from app.services.transacao_service import (
    criar_transacao,
    listar_transacoes,
    calcular_fluxo_caixa,
    pagar_conta,
    buscar_transacao_por_id
)

router = APIRouter(prefix="/financeiro", tags=["Financeiro"])

@router.get("/contas-pagar")
def listar_contas_pagar():
    return [
        t for t in listar_transacoes()
        if t.tipo == TipoTransacao.saida
    ]

@router.post("/contas-pagar")
def criar_conta_pagar(conta: ContaPagar):
    transacao = TransacaoCreate(
        **conta.dict(),
        tipo=TipoTransacao.saida
    )
    return criar_transacao(transacao)

@router.get("/contas-receber")
def listar_contas_receber():
    return [
        t for t in listar_transacoes()
        if t.tipo == TipoTransacao.entrada
    ]

@router.post("/contas-receber")
def criar_conta_receber(conta: ContaReceber):
    transacao = TransacaoCreate(
        **conta.dict(),
        tipo=TipoTransacao.entrada
    )
    return criar_transacao(transacao)

@router.get("/fluxo-caixa")
def fluxo_caixa():
    return calcular_fluxo_caixa()

@router.get("/contas-vencidas")
def contas_vencidas():
    hoje = date.today()

    return [
        t for t in listar_transacoes()
        if t.data_vencimento < hoje and t.status == "pendente"
    ]

@router.get("/contas/{transacao_id}")
def obter_transacao(transacao_id: UUID):
    transacao = buscar_transacao_por_id(transacao_id)

    if not transacao:
        raise HTTPException(
            status_code=404,
            detail="Transação não encontrada"
        )

    return transacao

@router.patch("/contas/{transacao_id}/pagar")
def marcar_como_pago(transacao_id: UUID):
    resultado = pagar_conta(transacao_id)

    if not resultado:
        raise HTTPException(
            status_code=404,
            detail="Transação não encontrada"
        )

    return resultado