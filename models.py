from pydantic import BaseModel, ConfigDict

class UsuarioSchema(BaseModel):
    id: int | None = None
    nome: str
    email: str
    telefone: str | None = None

    model_config = ConfigDict(from_attributes=True)


class ProdutoSchema(BaseModel):
    id: int | None = None
    nome: str
    descricao: str | None = None
    preco: float
    quantidade: int

    model_config = ConfigDict(from_attributes=True)


class TicketSchema(BaseModel):
    id: int | None = None
    titulo: str
    descricao: str
    prioridade: str
    categoria: str
    status: str
    criador_nome: str
    tecnico_nome: str | None = None

    model_config = ConfigDict(from_attributes=True)
