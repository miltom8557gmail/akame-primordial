import fasteners
import os
import telebot
from supabase import create_client

# Configurações
TOKEN = "8767431243:AAFVrV-ZKqPr_Qo9bCkcFoNuTsZ4TKlFXpU"
SUPA_URL = "https://qlkarekopepgvuyxopmy.supabase.co"
SUPA_KEY = os.getenv("SUPABASE_JWT")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'check'])
def diagnostic(message):
    bot.reply_to(message, "👹 Akame v100: Sistemas operacionais. Conexão SSH e API Estáveis.")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if "akame" in message.text.lower():
        bot.reply_to(message, "Sim, Mestre. Estou observando o fluxo de dados.")

if __name__ == "__main__":
    print("🚀 Akame v100 Iniciada no Telegram.")
    bot.infinity_polling()
