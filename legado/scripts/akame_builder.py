import fasteners
import requests
import os
import time

API_URL = "https://bfriplrxtleleplhpgwd.supabase.co/rest/v1/memoria?evento=eq.Comando%20Forja&order=created_at.desc&limit=1"
HEADERS = {
    "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcmlwbHJ4dGxlbGVwbGhwZ3dkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUxOTQ5NzcsImV4cCI6MjA5MDc3MDk3N30.6Hpk0Rxfj-JU-W5S1_52rETwa6dwqS0l5URBZFUgNkU",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcmlwbHJ4dGxlbGVwbGhwZ3dkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUxOTQ5NzcsImV4cCI6MjA5MDc3MDk3N30.6Hpk0Rxfj-JU-W5S1_52rETwa6dwqS0l5URBZFUgNkU"
}

last_id = ""

while True:
    try:
        r = requests.get(API_URL, headers=HEADERS)
        data = r.json()
        if data:
            cmd = data[0]['detalhes']
            created = data[0]['created_at']
            
            if created != last_id:
                if "cria" in cmd.lower() or "build" in cmd.lower():
                    print(f"🛠️ Akame: Ordem de construção recebida: {cmd}")
                    # Aqui a Akame usaria a IA para gerar o código (Próximo Passo)
                    # Por agora, ela cria um template de segurança
                    filename = "novo_modulo.sh"
                    with open(filename, "w") as f:
                        f.write("#!/bin/bash\necho '🔱 Módulo Gerado pela Akame'\n")
                    os.chmod(filename, 0o755)
                    print(f"✅ Akame: Arquivo {filename} forjado com sucesso.")
                
                last_id = created
    except:
        pass
    time.sleep(10)
