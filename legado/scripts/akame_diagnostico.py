import fasteners
import requests
import os

def check_status():
    print("🔱 --- RELATÓRIO DE STATUS AKAME --- 🔱")
    
    # 1. Verificar Supabase
    print("📡 Supabase: ", end="")
    try:
        url = "https://bfriplrxtleleplhpgwd.supabase.co/rest/v1/memoria?limit=1"
        headers = {
            "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcmlwbHJ4dGxlbGVwbGhwZ3dkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUxOTQ5NzcsImV4cCI6MjA5MDc3MDk3N30.6Hpk0Rxfj-JU-W5S1_52rETwa6dwqS0l5URBZFUgNkU",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcmlwbHJ4dGxlbGVwbGhwZ3dkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUxOTQ5NzcsImV4cCI6MjA5MDc3MDk3N30.6Hpk0Rxfj-JU-W5S1_52rETwa6dwqS0l5URBZFUgNkU"
        }
        r = requests.get(url, headers=headers)
        if r.status_code == 200: print("✅ CONECTADO")
        else: print("❌ ERRO DE CONEXÃO")
    except: print("⚠️ FALHA CRÍTICA")

    # 2. Verificar GitHub
    print("🐙 GitHub: ", end="")
    if os.path.exists(".git"):
        print("✅ REPOSITÓRIO LOCALIZADO")
    else:
        print("❌ PASTA .GIT NÃO ENCONTRADA")

    # 3. Verificar Processos Internos
    print("🧠 Agentes Internos: ", end="")
    # Checar se os scripts estão rodando em background
    check_brain = os.popen("pgrep -f akame_brain.py").read()
    check_worker = os.popen("pgrep -f forja_worker.sh").read()
    
    if check_brain and check_worker:
        print("✅ LEGIÃO ATIVA")
    else:
        print("⚠️ ALGUNS AGENTES ESTÃO DORMINDO")

    print("🔱 --------------------------------- 🔱")

if __name__ == "__main__":
    check_status()
