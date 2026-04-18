import fasteners
import os
from huggingface_hub import HfApi
from supabase import create_client

def validar():
    url = os.getenv("SUPABASE_URL", "https://bfriplrxtleleplhpgwd.supabase.co")
    key = os.getenv("SUPABASE_KEY")
    hf = os.getenv("HF_TOKEN")
    
    if not key or not hf:
        print("❌ [BLOQUEIO]: Chaves ausentes no ambiente.")
        return

    try:
        sb = create_client(url, key)
        sb.table("mission_logs").insert({"atividade": "Sincronia Forçada", "detalhes": {"engine": "v7.5"}}).execute()
        print("✅ [NEXUS]: Conexão estabelecida e registrada.")
    except Exception as e:
        print(f"⚠️ [AVISO]: Erro de registro: {e}")

if __name__ == "__main__":
    validar()
