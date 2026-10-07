import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from supabase import create_client, Client
from typing import Optional

app = FastAPI()

# Configuração do CORS para permitir requisições do seu GitHub Pages
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SUPABASE_URL = os.environ.get("SUPABASE_URL", "https://alogpdbuxferknvzpycf.supabase.co")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY", "sb_publishable_Yny_Wgv1W5LuC44f3bUGzw_Xejfmxu4")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

class VagaModel(BaseModel):
    id: str
    solicitacao: Optional[str] = ""
    nome_candidato: Optional[str] = ""
    necessidade: Optional[str] = ""
    estado: Optional[str] = "0. PROGRAMAÇÃO"
    resp_solicitacao: Optional[str] = ""
    obra: Optional[str] = ""
    funcao: Optional[str] = ""
    servico: Optional[str] = ""
    atividades: Optional[str] = ""
    prazo: Optional[str] = ""
    contrato: Optional[str] = ""
    trabalho_altura: Optional[str] = ""
    fardamento: Optional[str] = ""
    calcado: Optional[str] = ""
    contato: Optional[str] = ""
    contactado: Optional[str] = ""
    fazer_exame: Optional[str] = ""
    entrega_docs: Optional[str] = ""
    resultado_exame: Optional[str] = ""
    notas: Optional[str] = ""

@app.get("/")
def home():
    return {"status": "API Vagas Mirantes Operacional"}

@app.get("/vagas")
def listar_vagas():
    try:
        response = supabase.table("vagas").select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/vagas")
def salvar_vaga(vaga: VagaModel):
    try:
        dados = vaga.dict()
        response = supabase.table("vagas").upsert(dados).execute()
        return {"sucesso": True, "data": response.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
