import sys, time, re

def falar(texto):
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print("\n")

def analisar(entrada):
    entrada = entrada.lower()
    if "erro" in entrada or "falha" in entrada:
        return "🛠️ [DIAGNÓSTICO]: O GitHub tentou nos frear com tecnologias obsoletas. Já injetei o Java 21 e o Node 24. A falha é apenas o ensaio para a perfeição."
    elif "privacidade" in entrada:
        return "🛡️ [SOBERANIA]: Seus projetos não têm filtros. A criptografia de ponta no Termux garante que você é o único juiz do seu código."
    return "🔮 [ORÁCULO]: Sistema v4.6.1 em fase de translação. O império está se auto-corrigindo."

if len(sys.argv) > 1:
    falar(f"💬 [NEXUS]: {analisar(' '.join(sys.argv[1:]))}")
else:
    falar("🔱 [NEXUS]: Motor v4.6.1 Ativo. Aguardando ordens.")
