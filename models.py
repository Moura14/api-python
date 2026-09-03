from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func
from database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
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
    criado_em = Column(DateTime(timezone=True), server_default=func.now())



class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    prioridade = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    anexo_url = Column(String, nullable=True)
    status = Column(String, default="aberto")
    criado_por = Column(Integer, ForeignKey("usuarios.id"))
    criador_nome = Column(String, nullable=False)
    tecnico_responsavel_id = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    tecnico_nome = Column(String, nullable=True)
    data_criacao = Column(DateTime, default=datetime.utcnow)
    data_atualizacao = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    data_resolucao = Column(DateTime, nullable=True)

