from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from app.models.transacao import Transacao


def salvar(db: Session, transacao: Transacao):
    db.add(transacao)
    db.commit()
    db.refresh(transacao)
    return transacao


def listar(db: Session) -> List[Transacao]:
    return db.query(Transacao).all()


def buscar_por_id(db: Session, transacao_id: UUID):
    return db.query(Transacao).filter(Transacao.id == str(transacao_id)).first()


def atualizar(db: Session, transacao_id: UUID, novos_dados: dict):
    transacao = buscar_por_id(db, transacao_id)
    if transacao:
        for key, value in novos_dados.items():
            setattr(transacao, key, value)
        db.commit()
        db.refresh(transacao)
    return transacao
