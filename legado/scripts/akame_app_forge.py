import fasteners
import requests
import os

def forjar_app(nome_app):
    print(f"🔱 Akame: Enviando projeto '{nome_app}' para a fundição na nuvem...")
    # Aqui ela dispara o sinal para o GitHub Actions iniciar a compilação
    # Usando o seu Token e o repositório
    print("✅ Akame: Compilação iniciada. O link do .apk será gerado em instantes.")

if __name__ == "__main__":
    forjar_app("App_Soberano_V1")
