from datetime import date, timedelta
from app.core.database import SessionLocal, engine, Base
from app.models.transacao import Transacao, TipoTransacao, StatusTransacao
from uuid import uuid4

Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:
    hoje = date.today()
    
    dados_exemplo = [
        {
            "id": str(uuid4()),
            "descricao": "Aluguel do Escritório",
            "valor": 1500.00,
            "tipo": TipoTransacao.saida,
            "status": StatusTransacao.pendente,
            "data_vencimento": hoje + timedelta(days=5)
        },
        {
            "id": str(uuid4()),
            "descricao": "Venda de Software",
            "valor": 5000.00,
            "tipo": TipoTransacao.entrada,
            "status": StatusTransacao.pendente,
            "data_vencimento": hoje + timedelta(days=10)
        },
        {
            "id": str(uuid4()),
            "descricao": "Conta de Luz",
            "valor": 350.00,
            "tipo": TipoTransacao.saida,
            "status": StatusTransacao.pago,
            "data_vencimento": hoje - timedelta(days=3)
        },
        {
            "id": str(uuid4()),
            "descricao": "Serviço de Consultoria",
            "valor": 2500.00,
            "tipo": TipoTransacao.entrada,
            "status": StatusTransacao.pago,
            "data_vencimento": hoje - timedelta(days=7)
        },
        {
            "id": str(uuid4()),
            "descricao": "Internet Fibra",
            "valor": 150.00,
            "tipo": TipoTransacao.saida,
            "status": StatusTransacao.pendente,
            "data_vencimento": hoje - timedelta(days=2)
        }
    ]

    for dados in dados_exemplo:
        transacao = Transacao(**dados)
        db.add(transacao)
    
    db.commit()
    print("✅ Dados de exemplo adicionados com sucesso!")

finally:
    db.close()
