# 🔱 AKAME PRIMORDIAL - NÚCLEO DE COMANDO (V3)
import os
import telebot
import re
from datetime import datetime

def buscar_token_no_vault():
    caminho_vault = os.path.expanduser("~/AkamePortal/vault.py")
    if os.path.exists(caminho_vault):
        with open(caminho_vault, "r") as f:
            conteudo = f.read()
            # Busca ultra-flexível: aceita aspas simples ou duplas e espaços variados
            match = re.search(r'TELEGRAM_TOKEN"\]\s*=\s*"([^"]+)"', conteudo)
            if not match:
                match = re.search(r"TELEGRAM_TOKEN'\]\s*=\s*'([^']+)'", conteudo)
            
            if match:
                return match.group(1)
    return os.getenv("TELEGRAM_TOKEN")

TOKEN = buscar_token_no_vault()

if not TOKEN:
    print("❌ [ERRO]: Token do Telegram não encontrado! Verifique as aspas no vault.py.")
    exit()

bot = telebot.TeleBot(TOKEN)

def atualizar_memorando(acao):
    caminho = os.path.expanduser("~/AkamePrimordial/memorando/status_omni.md")
    data = datetime.now().strftime("%Y-%m-%d %H:%M")
    if os.path.exists(caminho):
        try:
            with open(caminho, "a") as f:
                f.write(f"\n- [{data}] {acao}")
        except:
            pass

@bot.message_handler(commands=['start', 'status'])
def boas_vindas(message):
    texto = (
        "🔱 **AKAME PRIMORDIAL: CONEXÃO ESTABELECIDA** 🔱\n\n"
        "Mestre, os protocolos de busca foram refinados.\n"
        "📍 **Status:** Online e Operacional\n"
        "🛡️ **Vault:** Vinculado com sucesso"
    )
    bot.reply_to(message, texto, parse_mode='Markdown')

@bot.message_handler(func=lambda m: True)
def escuta(message):
    msg = message.text.lower()
    if "oficina" in msg:
        bot.reply_to(message, "🛠️ **Oficina:** Aguardando especificações do APK.")
    else:
        atualizar_memorando(f"Telegram: {message.text}")
        bot.reply_to(message, "🗡️ Registrado no memorando.")

print("🔱 Akame Primordial despertando no Telegram...")
bot.polling()
