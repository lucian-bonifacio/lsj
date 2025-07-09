from fastapi import FastAPI
from routes.usuarios import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return {"mensagem": "API do Lar de São José funcionando!"}

@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.get("/hello")
def hello():
    return {"mensagem": "Olá, mundo!"}