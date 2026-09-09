from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, DateTime
from sqlalchemy.sql import func 
from database import Base

from datetime import datetime

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    senha = Column(String(255), nullable=False)
    telefone = Column(String(20))
    criado_em = Column(DateTime(timezone=True), server_default=func.now())


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(500))
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, default=0)



class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    prioridade = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    anexo_url = Column(String, nullable=True)

    status = Column(String, default="aberto")
    criado_por = Column(Integer, nullable=True, default=0)
    criador_nome = Column(String, nullable=True, default="Sistema")
    data_criacao = Column(DateTime, default=datetime.utcnow)
    data_atualizacao = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


