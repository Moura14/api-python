from datetime import timedelta

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import engine, get_db
from auth import ACCESS_TOKEN_EXPIRE_MINUTES, ACCESS_TOKEN_EXPIRE_MINUTES, criar_token_acesso, hash_senha, autenticar_usuario, get_current_user
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm



models.Base.metadata.create_all(bind=engine)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API rodando com PostgreSQL"}



@app.post("/register/", response_model=schemas.UsuarioResponse)
def criar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = models.Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha=hash_senha(usuario.senha),
        telefone=usuario.telefone
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

@app.get("/usuarios/", response_model=List[schemas.UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(models.Usuario).all()


@app.post("/login/", response_model=schemas.TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_usuario = autenticar_usuario(db, form_data.username, form_data.password)
    if not db_usuario:
        raise HTTPException(status_code=400, detail="Usuário ou senha incorretos")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = criar_token_acesso(
        data={"sub": db_usuario.email}, 
        expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "usuario": db_usuario
    }


@app.get("/me", response_model=schemas.UsuarioResponse)
async def get_me(usuario: models.Usuario = Depends(get_current_user)):
    return usuario

@app.post("/tickets/", response_model=schemas.TicketCreate)
def criar_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db), current_user: schemas.UsuarioResponse = Depends(get_current_user)):
    db_ticket = models.Ticket(
        titulo=ticket.titulo,
        descricao=ticket.descricao,
        prioridade=ticket.prioridade,
        categoria=ticket.categoria,
        anexo_url=ticket.anexo_url,
        status="Aberto",
        criado_por=current_user.id
    )
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

@app.post("/produtos/", response_model=schemas.ProdutoResponse)
def criar_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    db_produto = models.Produto(**produto.model_dump())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

@app.get("/produtos/", response_model=List[schemas.ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(models.Produto).all()