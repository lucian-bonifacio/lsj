
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from models.base import Base
from collections.abc import AsyncGenerator



DATABASE_URL = "postgresql+asyncpg://postgres:031980@localhost:5432/lsj"


# Função que cria o "motor" de conexão com o banco de dados
engine = create_async_engine(DATABASE_URL, echo=True)


# Cria a fábrica de sessões assíncronas
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)



async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session