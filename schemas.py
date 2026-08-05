from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Schema para Usuário
class UsuarioBase(BaseModel):
    nome: str
    email: str
    telefone: Optional[str] = None

class UsuarioCreate(UsuarioBase):
    pass

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