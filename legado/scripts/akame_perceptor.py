import fasteners
import os
import shutil
import requests

def sonda_profunda():
    print("👁️‍🗨️ [AKAME-PERCEPCION]: Ignorando bloqueios e acessando telemetria permitida...")
    
    # 1. Varredura de Hardware (Métodos Alternativos)
    total, used, free = shutil.disk_usage("/")
    
    # Em vez de psutil, usamos o comando 'free' do sistema via popen
    ram_data = os.popen("free -m").readlines()
    if len(ram_data) > 1:
        mem = ram_data[1].split()
        ram_livre = mem[3]
        ram_total = mem[1]
    else:
        ram_livre = "N/A"
        ram_total = "N/A"

    print(f"🌡️ CPU: Ativa (Monitoramento restrito pelo Android)")
    print(f"🧠 RAM: {ram_livre}MB Livres de {ram_total}MB")
    print(f"📂 DISCO: {free / (1024**3):.2f} GB disponiveis")

    # 2. Varredura de Conexoes (Usando 'ss' ou 'netstat' simplificado)
    conns = os.popen("netstat -ant 2>/dev/null | grep ESTABLISHED | wc -l").read().strip()
    print(f"🌐 Conexoes Ativas: {conns}")

    # 3. Integridade do Banco (Supabase)
    print("💾 Verificando Integridade da Memoria...")
    try:
        # Teste rápido de latência com o Supabase
        start = os.times().elapsed
        requests.get("https://bfriplrxtleleplhpgwd.supabase.co", timeout=5)
        latencia = (os.times().elapsed - start) * 1000
        print(f"✅ Supabase Latencia: {latencia:.2f}ms")
    except:
        print("⚠️ Supabase: Resposta lenta ou offline.")

if __name__ == "__main__":
    sonda_profunda()
