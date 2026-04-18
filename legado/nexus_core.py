from flask import Flask, jsonify, render_template_string, request
import subprocess, datetime

app = Flask(__name__)

# --- INTERFACE NIGHT RAID v12.0 (MEMÓRIA INTEGRADA) ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AKAME CORE | NIGHT RAID</title>
    <style>
        :root { --bg: #030303; --murasame: #d32f2f; --silver: #b0bec5; --border: rgba(211,47,47,0.4); }
        body { background: var(--bg); color: #fff; font-family: sans-serif; margin: 0; display: flex; flex-direction: column; height: 100vh; }
        .top-nav { display: flex; background: #000; border-bottom: 2px solid var(--murasame); overflow-x: auto; }
        .tab-btn { flex: 1; padding: 15px; color: var(--silver); background: none; border: none; font-weight: bold; cursor: pointer; white-space: nowrap; }
        .tab-btn.active { color: var(--murasame); border-bottom: 3px solid var(--murasame); }
        .content { flex: 1; padding: 20px; overflow-y: auto; }
        .card { background: rgba(20,20,20,0.8); border: 1px solid var(--border); padding: 15px; border-radius: 8px; margin-bottom: 15px; }
        .btn { width: 100%; padding: 12px; margin: 5px 0; background: #000; color: var(--murasame); border: 1px solid var(--murasame); font-weight: bold; border-radius: 4px; cursor: pointer; text-transform: uppercase; }
        .btn:active { background: var(--murasame); color: #000; }
        .input-box { width: 100%; background: #111; border: 1px solid var(--border); color: #fff; padding: 10px; margin-bottom: 10px; box-sizing: border-box; }
        #history { background: #000; border: 1px solid #333; height: 150px; overflow-y: auto; font-family: monospace; font-size: 0.8rem; padding: 10px; }
    </style>
</head>
<body>
    <div class="top-nav">
        <button class="tab-btn active" onclick="tab('core')">🛡️ NÚCLEO</button>
        <button class="tab-btn" onclick="tab('forge')">🔥 FORJA IA</button>
        <button class="tab-btn" onclick="tab('mem')">🧠 MEMÓRIA</button>
    </div>

    <div class="content">
        <div id="core" class="tab-content card">
            <h3>ARSENAL GITHUB</h3>
            <button class="btn" onclick="run('build-apk')">FORJAR APK DASHBOARD</button>
            <button class="btn" onclick="run('sync')">SINCRONIZAR GITHUB</button>
        </div>

        <div id="forge" class="tab-content card" style="display:none">
            <h3>FORJA LoRA & FFmpeg</h3>
            <textarea id="p" class="input-box" placeholder="Prompt NSFW/LoRA/Vídeo..."></textarea>
            <button class="btn" onclick="run('lora')">TREINAR LoRA (CIVITAI)</button>
            <button class="btn" onclick="run('ffmpeg')">MONTAR VÍDEO (FFMPEG)</button>
            <button class="btn" onclick="run('nsfw')">GERAR SEM FILTROS</button>
        </div>

        <div id="mem" class="tab-content card" style="display:none">
            <h3>CÓDICE DE REGISTROS</h3>
            <button class="btn" onclick="run('check-supabase')">TESTAR CONEXÃO SUPABASE</button>
            <div id="history">Aguardando dados...</div>
        </div>
    </div>

    <script>
        function tab(id) {
            document.querySelectorAll('.tab-content').forEach(c => c.style.display = 'none');
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.getElementById(id).style.display = 'block';
            event.currentTarget.classList.add('active');
        }
        function run(cmd) {
            let p = document.getElementById('p').value;
            fetch(`/api/exec?cmd=${cmd}&p=${p}`).then(r => r.json()).then(d => {
                document.getElementById('history').innerHTML += `<div>[${new Date().toLocaleTimeString()}] ${d.msg}</div>`;
            });
        }
    </script>
</body>
</html>
"""

@app.route('/api/exec')
def execute():
    cmd = request.args.get('cmd')
    p = request.args.get('p')
    # Lógica de conexão com o agente
    return jsonify({"msg": f"Comando {cmd} enviado à Forja do GitHub."})

if __name__ == '__main__': app.run(host='0.0.0.0', port=5001)
