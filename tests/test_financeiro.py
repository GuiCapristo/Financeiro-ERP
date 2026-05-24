from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_criar_conta_pagar():
    response = client.post("/financeiro/contas-pagar", json={
        "descricao": "Conta teste",
        "valor": 100,
        "status": "pendente",
        "data_vencimento": "2026-06-01"
    })

    assert response.status_code == 200
    data = response.json()

    assert "id" in data
    assert data["msg"] == "Transação criada com sucesso"

def test_listar_contas_pagar():
    response = client.get("/financeiro/contas-pagar")

    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_buscar_por_id():
    create = client.post("/financeiro/contas-pagar", json={
        "descricao": "Busca teste",
        "valor": 200,
        "status": "pendente",
        "data_vencimento": "2026-06-01"
    })

    transacao_id = create.json()["id"]

    response = client.get(f"/financeiro/contas/{transacao_id}")

    assert response.status_code == 200
    assert str(response.json()["id"]) == str(transacao_id)

def test_marcar_como_pago():
    create = client.post("/financeiro/contas-pagar", json={
        "descricao": "Pagamento teste",
        "valor": 300,
        "status": "pendente",
        "data_vencimento": "2026-06-01"
    })

    transacao_id = create.json()["id"]

    response = client.patch(f"/financeiro/contas/{transacao_id}/pagar")

    assert response.status_code == 200

    get = client.get(f"/financeiro/contas/{transacao_id}")
    assert get.json()["status"] == "pago"

def test_fluxo_caixa():
    response = client.get("/financeiro/fluxo-caixa")

    assert response.status_code == 200
    data = response.json()

    assert "total_entradas" in data
    assert "total_saidas" in data
    assert "saldo" in data

def test_valor_invalido():
    response = client.post("/financeiro/contas-pagar", json={
        "descricao": "Erro",
        "valor": -100,
        "status": "pendente",
        "data_vencimento": "2026-06-01"
    })

    assert response.status_code == 422

def test_campo_extra():
    response = client.post("/financeiro/contas-pagar", json={
        "descricao": "Teste",
        "valor": 100,
        "status": "pendente",
        "data_vencimento": "2026-06-01",
        "hack": "invasao"
    })

    assert response.status_code == 422