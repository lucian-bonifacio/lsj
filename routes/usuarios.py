from fastapi import APIRouter

router = APIRouter()

@router.get("/usuarios")
def usuarios():
    return {
        "nome": ['João', "Cleber"],
        "idade": [14, 25]    
    }