import fasteners
import requests
import time

# Onde o susto acontece
API_URL = "https://bfriplrxtleleplhpgwd.supabase.co/rest/v1/memoria"
HEADERS = {
    "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcmlwbHJ4dGxlbGVwbGhwZ3dkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUxOTQ5NzcsImV4cCI6MjA5MDc3MDk3N30.6Hpk0Rxfj-JU-W5S1_52rETwa6dwqS0l5URBZFUgNkU",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcmlwbHJ4dGxlbGVwbGhwZ3dkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUxOTQ5NzcsImV4cCI6MjA5MDc3MDk3N30.6Hpk0Rxfj-JU-W5S1_52rETwa6dwqS0l5URBZFUgNkU",
    "Content-Type": "application/json"
}

def disparar_susto(mensagem):
    data = {
        "evento": "AUDIO_GATILHO",
        "detalhes": mensagem
    }
    requests.post(API_URL, headers=HEADERS, json=data)
    print(f"🔱 Akame: Susto enviado para a rede: {mensagem}")

if __name__ == "__main__":
    disparar_susto("ESTOU MONITORANDO VOCÊ. SAIA DO MEU SISTEMA.")
