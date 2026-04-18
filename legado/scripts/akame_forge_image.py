import fasteners
import requests
import time

# URL Base sem o sufixo da tabela para teste de sanidade
SUPABASE_URL = "https://bfriplrxtleleplhpgwd.supabase.co/rest/v1/akame_generations"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcmlwbHJ4dGxlbGVwbGhwZ3dkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUxOTQ5NzcsImV4cCI6MjA5MDc3MDk3N30.6Hpk0Rxfj-JU-W5S1_52rETwa6dwqS0l5URBZFUgNkU"

def forjar_akame():
    print("🐍 [AKAME]: Recalibrando sensores de banco de dados...")
    
    prompt = "akame ga kill style, masterpiece, red eyes, murasame blade, dark aesthetic"
    
    payload = {
        "prompt": prompt,
        "status": "processing"
    }
    
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=minimal"
    }
    
    # Tentando disparar
    response = requests.post(SUPABASE_URL, json=payload, headers=headers)
    
    if response.status_code == 404:
        print("❌ [AVISO]: Mestre, a tabela 'akame_generations' não existe no Supabase.")
        print("💡 [SOLUÇÃO]: Vá ao Dashboard do Supabase > SQL Editor e rode:")
        print("   CREATE TABLE akame_generations (id serial primary key, prompt text, status text);")
    elif response.status_code in [201, 204]:
        print("🛡️ [SUCESSO]: Conexão estabelecida. A forja iniciou.")
    else:
        print(f"⚠️ Status: {response.status_code} - {response.text}")

if __name__ == "__main__":
    forjar_akame()
