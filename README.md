# Financeiro-ERP — Módulo Financeiro (API FastAPI)

Este repositório contém o módulo Financeiro de um ERP universitário. Ele é um serviço independente responsável pelo gerenciamento de contas a pagar, contas a receber e fluxo de caixa, expondo uma API FastAPI para consumo pelo Core e outros módulos via HTTP. Inclui também um Dashboard visual para apresentação dos dados.

---

## Estrutura do projeto

```
Financeiro-ERP/
├── README.md
├── .gitignore
├── requirements.txt
├── seed_data.py
└── app/
    ├── main.py
    ├── core/
    │   └── database.py
    ├── models/
    │   └── transacao.py
    ├── schemas/
    │   └── transacao_schema.py
    ├── repositories/
    │   └── transacao_repository.py
    ├── services/
    │   └── transacao_service.py
    ├── routers/
    │   └── financeiro_router.py
    └── static/
        └── index.html

tests/
├── __init__.py
├── pytest.ini
└── test_financeiro.py
```

---

## Stack

- FastAPI
- Uvicorn
- Pydantic
- SQLAlchemy (ORM para banco de dados)
- SQLite (banco de dados)
- Python 3.11+
- pytest

---

## Funcionalidades

### Contas a Pagar
- Criação de contas a pagar
- Listagem de contas a pagar

### Contas a Receber
- Criação de contas a receber
- Listagem de contas a receber

### Fluxo de Caixa
- Cálculo de entradas
- Cálculo de saídas
- Saldo consolidado

### Contas Vencidas
- Listagem de contas vencidas não pagas

### Pagamentos
- Marcar contas como pagas

### Consulta
- Buscar transação por ID

### Dashboard
- Interface visual para visualização dos dados
- Cards com totais de entradas, saídas e saldo
- Tabela com todas as transações

---

## Modelo de dados

### Transação

Campos principais:

- id
- descricao
- valor
- tipo (entrada ou saída)
- data_vencimento
- status (pendente ou pago)

---

## Como rodar o projeto

### 1) Clonar o repositório

```bash
git clone https://github.com/GuiCapristo/Financeiro-ERP
cd Financeiro-ERP
```

### 2) Criar ambiente virtual

```bash
python -m venv venv
```

### 3) Ativar o ambiente

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 4) Instalar dependências

```bash
pip install -r requirements.txt
```

### 5) (Opcional) Adicionar dados de exemplo

```bash
python seed_data.py
```

### 6) Executar a API

```bash
uvicorn app.main:app --reload --port 8002
```

Acessos:

- Dashboard (visual): http://localhost:8002
- Documentação Swagger: http://localhost:8002/docs
- Documentação Redoc: http://localhost:8002/redoc

---

## Endpoints

Todas as rotas estão sob /financeiro.

### Contas a pagar

- GET /financeiro/contas-pagar
- POST /financeiro/contas-pagar

### Contas a receber

- GET /financeiro/contas-receber
- POST /financeiro/contas-receber

### Fluxo de caixa

- GET /financeiro/fluxo-caixa

### Contas vencidas

- GET /financeiro/contas-vencidas

### Pagamento

- PATCH /financeiro/contas/{id}/pagar

### Consulta por ID

- GET /financeiro/contas/{id}

---

## Regras de negócio

- Transações do tipo entrada aumentam o saldo
- Transações do tipo saída diminuem o saldo
- Contas vencidas são aquelas com:
  - data_vencimento menor que a data atual
  - status igual a pendente
- Apenas contas pendentes podem ser marcadas como pagas

---

## Armazenamento de dados

Os dados são armazenados em banco de dados SQLite:

- Persistentes (não são perdidos ao reiniciar
- Arquivo `financeiro.db` criado na raiz do projeto
- ORM SQLAlchemy para manipulação dos dados

---

## Testes

```bash
python -m pytest tests/ -v
```

---

## Integração com o Core

O módulo foi projetado para funcionar como um serviço independente, sendo consumido pelo Core via HTTP.

---

## Autores

- Guilherme Capristo
- Marcos Vinícius

---

## Observações

Este projeto foi desenvolvido para fins acadêmicos, com foco em arquitetura modular e separação de responsabilidades em sistemas distribuídos.
