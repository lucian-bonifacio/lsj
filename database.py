from sqlalchemy.ext.asyncio import create_async_engine
from models.usuario import Base  # importa a Base usada pelo modelo
import asyncio

# URL de conexão com o banco (ajuste se o nome do banco ou senha for diferente)
DATABASE_URL = "postgresql+asyncpg://postgres:031980@localhost:5432/lsj"

# Cria o "motor" do banco (conexão)
engine = create_async_engine(DATABASE_URL)

# Função para criar as tabelas
async def criar_tabelas():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Executa a função assíncrona se rodar esse arquivo diretamente
if __name__ == "__main__":
    asyncio.run(criar_tabelas())
