from pydantic import BaseModel, field_validator, ConfigDict
from datetime import datetime
from typing import Optional

# Schema para Usuário
class UsuarioBase(BaseModel):
    nome: str
    email: str
    telefone: Optional[str] = None

class UsuarioCreate(UsuarioBase):
    senha: str

    @field_validator('senha')
    @classmethod
    def validar_senha(cls, v):
        if len(v) < 6:
            raise ValueError('Senha deve ter no mínimo 6 caracteres')
        if len(v) > 72:
            raise ValueError('Senha não pode ter mais de 72 caracteres')
        return v

class UsuarioResponse(UsuarioBase):
    id: int
    criado_em: datetime
    
    class Config:
       model_config = ConfigDict(from_attributes=True)

class UsuarioLogin(BaseModel):
    email: str
    senha: str 

class TicketCreate(BaseModel):
    titulo: str
    descricao: str
    prioridade: str
    categoria: str
    anexo_url: Optional[str] = None


class TicketResponse(TicketCreate):
    id: int
    titulo: str
    descricao: str
    prioridade: str
    categoria: str
    anexo_url: Optional[str] = None
    status: str
    criado_por: int
    criador_nome: str
    tecnico_responsavel_id: Optional[int] = None
    tecnico_nome: Optional[str] = None
    data_criacao: datetime
    data_atualizacao: datetime
    data_resolucao: Optional[datetime] = None


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    usuario: UsuarioResponse

# Schema para Produto
class ProdutoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: float
    quantidade: int

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoResponse(ProdutoBase):
    id: int
    criado_em: datetime
    
    class Config:
        model_config = ConfigDict(from_attributes=True)