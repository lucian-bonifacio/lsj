from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração do logger
logger.add(
    "logs/api.log",
    rotation="500 MB",
    retention="10 days",
    level="DEBUG" if os.getenv("DEBUG", "false").lower() == "true" else "INFO"
)

# Inicialização da aplicação FastAPI
app = FastAPI(
    title="LSJ - Sistema de Gestão Financeira",
    description="API para o sistema de gestão financeira do Lar de São José",
    version="0.1.0"
)

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especificar origens permitidas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    """Endpoint para verificar se a API está funcionando"""
    return {"status": "ok", "message": "API funcionando corretamente"}


@app.get("/")
async def root():
    """Endpoint raiz da API"""
    return {
        "message": "Olá, mundo!",
        "docs": "/docs",  # Link para a documentação Swagger
        "redoc": "/redoc"  # Link para a documentação ReDoc
    }