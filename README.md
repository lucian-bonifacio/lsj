# LSJ — Sistema de Gestão Financeira

## Sobre o Projeto

O Sistema de Gestão Financeira LSJ é uma solução completa para a administração financeira do Lar de São José, oferecendo funcionalidades de conciliação bancária e geração de relatórios oficiais. Esta plataforma foi desenvolvida para otimizar processos financeiros e garantir uma gestão transparente e eficiente.

## Stack Tecnológica

### Backend
- **Python**
  - FastAPI (Framework web de alta performance)
  - SQLAlchemy (ORM para interação com banco de dados)
  - Pydantic (Validação de dados e configurações)
  - Alembic (Migrações de banco de dados)

### Banco de Dados
- **PostgreSQL**

### Frontend
- **React**
  - Vite (Build tool e ambiente de desenvolvimento)
  - Tailwind CSS (Framework CSS utilitário)

## Funcionalidades Principais

- Gestão financeira completa
- Conciliação bancária
- Geração de relatórios oficiais
- Interface intuitiva e responsiva

## Configuração do Ambiente Virtual (Windows/PowerShell)

Para criar e ativar o ambiente virtual Python do projeto:

1. Certifique-se de que o Python 3.11+ está instalado (versão atual: Python 3.13.3):  
   ```powershell
   python --version
   ```

2. Crie o ambiente virtual dentro da pasta do projeto:  
   ```powershell
   py -3 -m venv .venv
   ```

3. Ative o ambiente virtual:  
   ```powershell
   .venv\Scripts\Activate.ps1
   ```

4. Valide que o ambiente está ativo (o prompt exibirá `(.venv)` no início) e que o `pip` está vinculado ao venv:  
   ```powershell
   python -m pip -V
   ```

> Observação: a pasta `.venv` **não deve ser versionada** (já está listada no `.gitignore`).

## Instalação de dependências (Windows)

Após ativar o ambiente virtual, instale as dependências do backend:

1. Navegue até a pasta do projeto:
   ```powershell
   cd C:\caminho\para\lsj
   ```

2. Instale as dependências do backend:
   ```powershell
   pip install -r backend\requirements.txt
   ```

3. Verifique se as dependências foram instaladas corretamente:
   ```powershell
   pip list
   ```

## Executando o Backend

Para iniciar o servidor de desenvolvimento com hot-reload:

1. Certifique-se de que o ambiente virtual está ativado

2. Execute o servidor Uvicorn a partir da raiz do projeto:
   ```powershell
   uvicorn app.main:app --reload --port 8000 --app-dir backend
   ```

3. Acesse a API em [http://localhost:8000](http://localhost:8000)

4. A documentação interativa está disponível em:
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)


## 🐳 Execução com Docker

Este projeto oferece uma maneira alternativa de rodar o backend usando Docker, ideal para padronizar o ambiente de desenvolvimento entre diferentes máquinas.

### 🔧 Pré-requisitos

- Docker Desktop instalado e rodando
- Terminal com suporte a comandos `docker`

### 🚀 Passo a passo

1. Acesse a pasta `backend`:
   ```bash
   cd backend
   ```

2. Construa a imagem:
   ```bash
   docker build -t lsj-backend-dev .
   ```

3. Execute o container:
   ```bash
   docker run -it --rm -p 8000:8000 -v $(pwd)/app:/app/app lsj-backend-dev uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```


