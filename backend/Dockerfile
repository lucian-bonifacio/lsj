# Stage de Build para instalar dependências
FROM python:3.11-slim-buster AS builder

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Stage de Runtime para a aplicação FastAPI
FROM python:3.11-slim-buster AS runtime

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia as dependências instaladas do stage de build
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copia o código da aplicação para o diretório de trabalho
# O contexto da cópia é a pasta 'backend' devido à estrutura do projeto
COPY app ./app

# Expõe a porta que a aplicação FastAPI irá rodar
EXPOSE 8000

# Comando para iniciar a aplicação com Uvicorn e hot-reload
# --app-dir backend é importante para que o uvicorn encontre o módulo main.py corretamente
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--app-dir", "."]