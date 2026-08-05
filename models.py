from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func
from database import Base

# Exemplo de modelo - Tabela de usuários
class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    telefone = Column(String(20))
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    
# Exemplo de modelo - Tabela de produtos
class Produto(Base):
    __tablename__ = "produtos"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(500))
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, default=0)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())