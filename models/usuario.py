from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import DeclarativeBase

# Essa classe é a base que dá os "poderes mágicos" para nossa tabela
class Base(DeclarativeBase):
    pass

# Essa é a nossa tabela de usuários!
class Usuario(Base):
    __tablename__ = "usuarios"  # nome da tabela no banco

    id = Column(Integer, primary_key=True, index=True)  # ID único de cada usuário
    nome = Column(String, nullable=False)               # Nome do usuário (não pode ser nulo)
    email = Column(String, unique=True, nullable=False) # E-mail (único e obrigatório)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())  # Data da criação
