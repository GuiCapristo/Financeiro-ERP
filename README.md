# Módulo Financeiro - ERP com FastAPI

Este projeto foi desenvolvido como parte da disciplina de **Programação de Sistemas Distribuídos**, com o objetivo de implementar um módulo financeiro de um sistema ERP utilizando a framework **FastAPI**.

---

## Visão Geral

O sistema permite o gerenciamento de transações financeiras, incluindo contas a pagar, contas a receber e cálculo de fluxo de caixa, seguindo boas práticas de organização em camadas (routers, services, repositories e schemas).

---

## Funcionalidades

### Contas a Pagar
- Criação de contas a pagar
- Listagem de contas a pagar

### Contas a Receber
- Criação de contas a receber
- Listagem de contas a receber

### Fluxo de Caixa
- Cálculo consolidado de:
  - Total de entradas
  - Total de saídas
  - Saldo final

### Contas Vencidas
- Identificação de contas vencidas com status pendente

### Pagamento de Contas
- Atualização do status de transações para "pago"

### Consulta de Transações
- Busca de transações por identificador único (UUID)

---

## Estrutura do Projeto

```
app/
├── main.py
├── core/
├── models/
│ └── transacao.py
├── schemas/
│ └── transacao_schema.py
├── repositories/
│ └── transacao_repository.py
├── services/
│ └── transacao_service.py
├── routers/
│ └── financeiro_router.py
tests/
├── test_financeiro.py
requirements.txt
```

---

## Tecnologias Utilizadas

- Python 3.11+
- FastAPI
- Pydantic
- Pytest

---

## Execução do Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/modulo-financeiro.git
cd modulo-financeiro

2. Criar ambiente virtual
python -m venv venv

3. Ativar o ambiente virtual

Windows

venv\Scripts\activate

Linux / macOS

source venv/bin/activate
4. Instalar dependências
pip install -r requirements.txt
5. Executar a aplicação
uvicorn app.main:app --reload
Documentação da API

Após iniciar o servidor, a documentação interativa estará disponível em:

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
Testes

Para executar os testes automatizados:

pytest
Endpoints Principais
Método	Endpoint	Descrição
GET	/financeiro/contas-pagar	Lista contas a pagar
POST	/financeiro/contas-pagar	Cria conta a pagar
GET	/financeiro/contas-receber	Lista contas a receber
POST	/financeiro/contas-receber	Cria conta a receber
GET	/financeiro/fluxo-caixa	Retorna o fluxo de caixa
GET	/financeiro/contas-vencidas	Lista contas vencidas
PATCH	/financeiro/contas/{id}/pagar	Marca conta como paga
Regras de Negócio
Transações do tipo "entrada" aumentam o saldo
Transações do tipo "saida" reduzem o saldo
Uma conta é considerada vencida quando:
A data de vencimento é anterior à data atual
O status é "pendente"
Apenas transações pendentes podem ser marcadas como pagas
Autores
Seu Nome
Nome dos integrantes do grupo
Observações

O sistema utiliza armazenamento em memória (lista em Python), não havendo persistência de dados após reinicialização da aplicação.
