import fasteners
from flask import Flask, render_template_string
from vault.akame_vault import AkameVault

app = Flask(__name__)

HTML_DASHBOARD = """
<!DOCTYPE html>
<html>
<head>
    <title>AKAME OMNIPOTENCE V100</title>
    <style>
        body { background: #050505; color: #00ff00; font-family: monospace; padding: 20px; }
        .card { border: 1px solid #333; padding: 15px; margin: 10px; background: #0a0a0a; border-left: 5px solid #f00; }
        h1 { color: #f00; text-shadow: 0 0 10px #f00; }
        .status-on { color: #0f0; }
        .status-off { color: #f00; }
    </style>
</head>
<body>
    <h1>🔱 AKAME OMNIPOTENCE V100</h1>
    <div class="card">
        <h3>🛰️ Conexões Ativas</h3>
        <p>Supabase: {{ status.Supabase }}</p>
        <p>Telegram: {{ status.Telegram }}</p>
        <p>HuggingFace: {{ status.HuggingFace }}</p>
    </div>
    <div class="card">
        <h3>⚔️ Agentes em Operação</h3>
        <ul>
            <li>Nexus Bridge: <span class="status-on">ONLINE</span></li>
            <li>Sentinel Bot: <span class="status-on">ATIVO</span></li>
            <li>ImageForge: <span class="status-on">AGUARDANDO PROMPT</span></li>
        </ul>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    status = {
        "Supabase": "CONECTADO" if AkameVault.SUPABASE_URL != "None" else "ERRO",
        "Telegram": "CONECTADO" if AkameVault.TELEGRAM_TOKEN != "None" else "ERRO",
        "HuggingFace": "CONECTADO" if AkameVault.HF_TOKEN != "Pendente" else "PENDENTE"
    }
    return render_template_string(HTML_DASHBOARD, status=status)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=AkameVault.NEXUS_PORT)
