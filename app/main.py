from fastapi import FastAPI
from app.routers.financeiro_router import router

app = FastAPI(title="Módulo Financeiro")

app.include_router(router)