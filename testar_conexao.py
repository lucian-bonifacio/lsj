import asyncio
from sqlalchemy.ext.asyncio import create_async_engine

# URL de conexão no formato do asyncpg
DATABASE_URL = "postgresql+asyncpg://postgres:031980@localhost:5432/lsj"

# Cria a engine assíncrona
engine = create_async_engine(DATABASE_URL, echo=True)

async def testar_conexao():
    try:
        async with engine.begin() as conn:
            print("✅ Conexão bem-sucedida com o banco de dados!")
    except Exception as e:
        print("❌ Erro ao conectar:", e)

if __name__ == "__main__":
    asyncio.run(testar_conexao())
