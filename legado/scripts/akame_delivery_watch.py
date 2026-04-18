import fasteners
import requests
import time
import os

URL = "https://bfriplrxtleleplhpgwd.supabase.co/rest/v1/akame_generations?select=image_url&status=eq.completed&order=id.desc&limit=1"
HEADERS = {
    "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcmlwbHJ4dGxlbGVwbGhwZ3dkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUxOTQ5NzcsImV4cCI6MjA5MDc3MDk3N30.6Hpk0Rxfj-JU-W5S1_52rETwa6dwqS0l5URBZFUgNkU",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJmcmlwbHJ4dGxlbGVwbGhwZ3dkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUxOTQ5NzcsImV4cCI6MjA5MDc3MDk3N30.6Hpk0Rxfj-JU-W5S1_52rETwa6dwqS0l5URBZFUgNkU"
}

print("🐍 [AKAME]: Sentinela de entrega ativado. Aguardando manifestação visual...")

while True:
    response = requests.get(URL, headers=HEADERS)
    data = response.json()
    
    if data and data[0].get("image_url"):
        os.system("termux-tts-speak 'Mestre, a forja foi concluída. Minha imagem está disponível no portal.'")
        print(f"✨ [PRONTA]: {data[0]['image_url']}")
        break
    time.sleep(10) # Verifica a cada 10 segundos
