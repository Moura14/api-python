from pydantic import BaseModel, field_validator
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
        from_attributes = True

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
        from_attributes = True