from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.core.config import VERSION, ORIGINS
from app.api.v1.endpoints import router as api_router

# Inicialização da aplicação FastAPI
app = FastAPI()

# Configuração do middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montagem de arquivos estáticos
app.mount("/static", StaticFiles(directory="src/static"), name="static")

# Configuração do Jinja2Templates
templates = Jinja2Templates(directory="src/templates")

# Inclusão das rotas da API
app.include_router(api_router, prefix='/api/v1')

# Rota para obter a versão da aplicação
@app.get("/api/version")
async def get_app_config():
    return {
        "version": VERSION,
    }

# Rota para a página inicial
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )