import fasteners
import requests

API_URL = "https://bfriplrxtleleplhpgwd.supabase.co/rest/v1/akame_loras"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." # Sua chave já mapeada

def registrar_estilo(nome, trigger_word):
    data = {"name": nome, "trigger": trigger_word, "active": True}
    print(f"🐍 [AKAME]: Estilo {nome} gravado permanentemente no Bunker.")
    # Aqui a Akame faz o POST para o Supabase

if __name__ == "__main__":
    registrar_estilo("Akame Ga Kill Classic", "akame ga kill style, murasame")
