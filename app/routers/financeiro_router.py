from fastapi import APIRouter, HTTPException, Depends
from datetime import date
from uuid import UUID
from sqlalchemy.orm import Session

from app.schemas.transacao_schema import (
    TransacaoCreate,
    ContaPagar,
    ContaReceber,
    TipoTransacao,
    StatusTransacao
)

from app.services.transacao_service import (
    criar_transacao,
    listar_transacoes,
    calcular_fluxo_caixa,
    pagar_conta,
    buscar_transacao_por_id
)

from app.core.database import get_db

router = APIRouter(prefix="/financeiro", tags=["Financeiro"])


@router.get("/contas-pagar")
def listar_contas_pagar(db: Session = Depends(get_db)):
    return [
        t for t in listar_transacoes(db)
        if t["tipo"] == TipoTransacao.saida
    ]


@router.post("/contas-pagar")
def criar_conta_pagar(conta: ContaPagar, db: Session = Depends(get_db)):
    transacao = TransacaoCreate(
        **conta.model_dump(),
        tipo=TipoTransacao.saida
    )
    return criar_transacao(db, transacao)


@router.get("/contas-receber")
def listar_contas_receber(db: Session = Depends(get_db)):
    return [
        t for t in listar_transacoes(db)
        if t["tipo"] == TipoTransacao.entrada
    ]


@router.post("/contas-receber")
def criar_conta_receber(conta: ContaReceber, db: Session = Depends(get_db)):
    transacao = TransacaoCreate(
        **conta.model_dump(),
        tipo=TipoTransacao.entrada
    )
    return criar_transacao(db, transacao)


@router.get("/fluxo-caixa")
def fluxo_caixa(db: Session = Depends(get_db)):
    return calcular_fluxo_caixa(db)


@router.get("/contas-vencidas")
def contas_vencidas(db: Session = Depends(get_db)):
    hoje = date.today()
    resultado = []
    for t in listar_transacoes(db):
        t_data = date.fromisoformat(t["data_vencimento"])
        if t_data < hoje and t["status"] == StatusTransacao.pendente:
            resultado.append(t)
    return resultado


@router.get("/contas/{transacao_id}")
def obter_transacao(transacao_id: UUID, db: Session = Depends(get_db)):
    transacao = buscar_transacao_por_id(db, transacao_id)
    if not transacao:
        raise HTTPException(
            status_code=404,
            detail="Transação não encontrada"
        )
    return transacao


@router.patch("/contas/{transacao_id}/pagar")
def marcar_como_pago(transacao_id: UUID, db: Session = Depends(get_db)):
    resultado = pagar_conta(db, transacao_id)
    if not resultado:
        raise HTTPException(
            status_code=404,
            detail="Transação não encontrada"
        )
    return resultado
