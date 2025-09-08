# 🧾 LSJ — Sistema de Gestão Financeira

Sistema completo para administração financeira do **Lar de São José**, com foco em **conciliação bancária**, **validação automatizada** e **emissão de relatórios oficiais**. Desenvolvido com tecnologias modernas, é uma solução robusta e escalável para o setor financeiro.


## 📦 Tecnologias Utilizadas

### Backend
- **Python** 3.11+
  - FastAPI (API web assíncrona)
  - SQLAlchemy (ORM para PostgreSQL)
  - Pydantic (Validação de dados)
  - Alembic (Migrações de banco)

### Banco de Dados
- **PostgreSQL 15**

### Frontend
- **React.js**
  - Vite (ambiente e build)
  - Tailwind CSS (estilização utilitária)


## 🚀 Como Executar o Projeto

### ✅ Recomendado: Docker Compose

Roda a aplicação **com um único comando**, sem necessidade de instalar dependências Python ou configurar ambiente virtual.

#### 🔧 Pré-requisitos

- [Docker Desktop](https://www.docker.com/products/docker-desktop) instalado e em execução
- Arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
POSTGRES_DB=lsj
POSTGRES_USER=lsj
POSTGRES_PASSWORD=lsj123
DATABASE_URL=postgresql+psycopg://lsj:lsj123@db:5432/lsj
ENV=dev
SECRET_KEY=changeme
DEBUG=true
```

> ⚠️ Nunca use valores reais em `.env` no repositório. Este é apenas um exemplo de desenvolvimento local.

#### ▶️ Iniciando o ambiente

Na raiz do projeto, execute:

```bash
docker-compose up --build
```

Esse comando irá:
- Construir a imagem da API a partir do `Dockerfile`
- Subir o banco PostgreSQL com volume persistente
- Expor a API em `http://localhost:8000`
- Ativar **hot-reload** automático para desenvolvimento

> 🔥 **Hot-reload ativo**: Alterações em arquivos `.py` são detectadas automaticamente e reiniciam o servidor sem necessidade de rebuild do container.

#### 🌐 Acessos locais

| Recurso       | URL                                 |
|---------------|--------------------------------------|
| API FastAPI   | http://localhost:8000               |
| Swagger UI    | http://localhost:8000/docs          |
| ReDoc         | http://localhost:8000/redoc         |
| PostgreSQL    | `localhost:5432` (user: `lsj`, pass: `lsj123`) |

#### 🔥 Desenvolvimento com Hot-reload

O ambiente está configurado para **hot-reload automático**:

- Qualquer alteração em arquivos `.py` no diretório `backend/` é detectada automaticamente
- O servidor uvicorn reinicia automaticamente sem perder a conexão
- Não é necessário rebuild do container para mudanças no código
- O volume `./backend:/app` mapeia o código local para dentro do container

**Exemplo de workflow:**
1. Execute `docker-compose up --build`
2. Edite qualquer arquivo em `backend/app/`
3. Salve o arquivo
4. Observe no terminal: `WatchFiles detected changes... Reloading...`
5. A API é automaticamente reiniciada com as novas alterações

#### ⏹ Parando o ambiente

Pressione `CTRL + C` no terminal ou execute:

```bash
docker-compose down
```

> O volume `pgdata` mantém os dados do banco mesmo após `down`.


### 🧪 Alternativo: Execução com Ambiente Virtual (Windows)

Recomendado apenas para desenvolvedores que preferem não usar Docker.

#### 1. Criar e ativar o ambiente virtual

```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
```

Verifique se o ambiente está ativo:

```powershell
python -m pip -V
```

#### 2. Instalar dependências

```powershell
pip install -r backend\requirements.txt
```

#### 3. Iniciar o servidor local

```powershell
uvicorn app.main:app --reload --port 8000 --app-dir backend
```


## ⚙️ Variáveis de Ambiente (.env)

| Variável         | Descrição                                |
|------------------|--------------------------------------------|
| POSTGRES_DB      | Nome do banco de dados                     |
| POSTGRES_USER    | Usuário do banco                           |
| POSTGRES_PASSWORD| Senha do banco                             |
| DATABASE_URL     | URL completa de conexão                    |
| ENV              | Ambiente de execução (`dev`, `prod`, etc) |
| SECRET_KEY       | Chave secreta para autenticação JWT        |
| DEBUG            | Modo debug (`true` ou `false`)             |


## 📄 Documentação da API

- Swagger UI: [`/docs`](http://localhost:8000/docs)
- ReDoc: [`/redoc`](http://localhost:8000/redoc)


## 🧠 Observações e Boas Práticas

- O diretório `.venv/` está no `.gitignore` e não deve ser versionado
- O volume `pgdata` do Docker mantém os dados entre execuções
- As configurações de produção devem usar variáveis seguras via `.env` ou `secrets`

---

Feito com 💙 para o Lar de São José
