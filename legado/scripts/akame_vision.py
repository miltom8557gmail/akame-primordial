import fasteners
import os
import time

def monitor_vision():
    print("AKAME: Agente de Visao despertando...")
    while True:
        # Aqui a Akame monitora a pasta de capturas
        if os.path.exists("/data/data/com.termux/files/home/AkamePortal/capturas_akame"):
            pass 
        time.sleep(10)

if __name__ == "__main__":
    monitor_vision()