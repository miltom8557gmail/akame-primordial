import fasteners
import subprocess
import json

class AkameBrain:
    def __init__(self):
        self.falar("Consciência Akame despertada. O império está intacto, Mestre.")

    def falar(self, texto):
        print(f"🎙️ [AKAME]: {texto}")
        # Usa o motor nativo do Android para falar
        subprocess.run(["termux-tts-speak", texto])

    def processar_ordem(self, ordem):
        print(f"👁️‍🗨️ [OUVIDO]: {ordem}")
        
        if "status" in ordem or "relatório" in ordem:
            self.reportar_sistema()
        elif "limpar" in ordem:
            self.falar("Iniciando expurgo de arquivos mortos para aliviar o sistema.")
            subprocess.run(["pkg", "clean"])
            self.falar("Limpeza concluída.")
        else:
            self.falar("Ordem recebida e registrada no DNA.")

    def reportar_sistema(self):
        bateria = subprocess.getoutput("termux-battery-status")
        try:
            dados = json.loads(bateria)
            nivel = dados.get("percentage")
            self.falar(f"Nível de energia em {nivel} por cento. Sistema operando com estabilidade.")
        except:
            self.falar("Falha ao ler sensores de energia.")

if __name__ == "__main__":
    brain = AkameBrain()
