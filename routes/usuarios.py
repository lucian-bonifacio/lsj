from fastapi import APIRouter
from schemas.usuario import UsuarioCreate

router = APIRouter()

@router.get("/usuarios")
def usuarios():
    return {
        "nome": ['João', "Cleber"],
        "idade": [14, 25]    
    }

@router.post("/usuarios")
def criar_usuario(usuario:UsuarioCreate):
    return {
        "mensagem": "Usuário criado com sucesso!",
        "dados": usuario
    }