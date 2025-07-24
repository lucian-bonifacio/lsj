import os

# Palavras proibidas em qualquer parte do caminho
IGNORAR = {'.venv', 'venv','__pycache__', '.git', '.vscode', '.DS_Store', 'Thumbs.db'}

def deve_ignorar(caminho):
    partes = caminho.split(os.sep)
    return any(p in IGNORAR for p in partes)

def listar_estrutura(caminho='.', prefixo=''):
    if deve_ignorar(caminho):
        return

    try:
        itens = sorted(os.listdir(caminho))
    except PermissionError:
        return

    itens_filtrados = [item for item in itens if not deve_ignorar(os.path.join(caminho, item))]

    for i, item in enumerate(itens_filtrados):
        caminho_completo = os.path.join(caminho, item)
        is_ultimo = (i == len(itens_filtrados) - 1)
        conector = '└── ' if is_ultimo else '├── '

        print(prefixo + conector + item)

        if os.path.isdir(caminho_completo):
            novo_prefixo = prefixo + ('    ' if is_ultimo else '│   ')
            listar_estrutura(caminho_completo, novo_prefixo)

if __name__ == '__main__':
    listar_estrutura()
