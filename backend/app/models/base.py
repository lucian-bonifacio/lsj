from sqlalchemy.orm import DeclarativeBase

# O DeclarativeBase é uma classe que serve de base para todas as nossas models
# Ele fornece a funcionalidade necessária para que o SQLAlchemy possa mapear as classes Python para tabelas do banco de dados
# e vice-versa, facilitando a manipulação dos dados de forma orientada a objetos

# A classe Base herda de DeclarativeBase, permitindo que todas as models que herdarem de Base
# sejam reconhecidas pelo SQLAlchemy como entidades persistentes no banco de dados.
class Base(DeclarativeBase):
    pass



