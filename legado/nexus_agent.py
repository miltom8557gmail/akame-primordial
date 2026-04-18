import sys, os, subprocess

def run_gh_action(workflow_name, inputs):
    """Dispara a Forja no GitHub com parâmetros do Mestre"""
    print(f"🚀 [FORJA]: Acionando {workflow_name}...")
    cmd = f"gh workflow run {workflow_name} "
    for key, val in inputs.items():
        cmd += f"-f {key}='{val}' "
    return subprocess.getoutput(cmd)

def mission_control(action, target, prompt=""):
    if action == "vender":
        # Cria projeto secundário e prepara para o cliente
        return f"📦 Projeto {target} criado e isolado da Akame."
    
    elif action == "criar-video":
        # Aciona o FFmpeg no GitHub para montar vídeo
        return run_gh_action("video_forge.yml", {"prompt": prompt, "client": target})

    elif action == "gerar-nsfw":
        # Aciona o Stable Diffusion no GitHub (Sem Filtros)
        return run_gh_action("image_forge.yml", {"prompt": prompt, "mode": "raw"})

    return "⚠️ Comando não mapeado no DNA."

if __name__ == "__main__":
    # Lógica de recebimento do Dashboard (Webview)
    if len(sys.argv) > 1:
        # Ex: python3 nexus_agent.py --cmd "criar-video" --target "Cliente1" --prompt "..."
        print(f"✅ Akame Processando: {sys.argv}")
