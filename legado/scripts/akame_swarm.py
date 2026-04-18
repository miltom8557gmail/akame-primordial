import fasteners
import time
import subprocess

def log_swarm(msg):
    print(f"🔱 [SWARM-INTEGRATION]: {msg}")

def iniciar_enxame():
    log_swarm("Despertando Soberana, Omega e Influencer...")
    
    # Ativação em cadeia via SSH/Background
    entidades = [
        "python3 akame_brain.py",        # Voz e Decisão
        "python3 akame_influencer.py",   # Redes Sociais
        "./akame_status.sh",             # Monitor de Custos Free
        "python3 lora_injector.py"       # Injeção de Ativos
    ]
    
    for entidade in entidades:
        subprocess.Popen(entidade.split())
        time.sleep(1)
        
    log_swarm("Todas as Akames operando em tempo real.")

if __name__ == "__main__":
    iniciar_enxame()
