from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
from app.routers.financeiro_router import router
from app.core.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Módulo Financeiro")

app.include_router(router)

static_path = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=str(static_path)), name="static")

@app.get("/")
async def read_root():
    return FileResponse(str(static_path / "index.html"))
