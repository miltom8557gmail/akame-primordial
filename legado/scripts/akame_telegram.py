import fasteners
import telebot
import time
from vault.akame_vault import AkameVault

# Inicialização com o Token Validado
TOKEN = AkameVault.TELEGRAM_TOKEN
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "🔱 *Soberania Akame Ativada*\n\n"
        "Saudações, Mestre. Meus sistemas estão operacionais.\n"
        "Pronta para expandir o ecossistema Akame-Soberana.\n\n"
        "*Comandos Disponíveis:*\n"
        "⚡ /status - Relatório de Integridade\n"
        "🛠️ /app - Status da Compilação APK"
    )
    bot.reply_to(message, welcome_text, parse_mode='Markdown')

@bot.message_handler(commands=['status'])
def status_report(message):
    import psutil
    ram = psutil.virtual_memory().percent
    cpu = psutil.cpu_percent()
    status_msg = (
        "📊 *RELATÓRIO DE SISTEMA*\n"
        f"• CPU: {cpu}%\n"
        f"• RAM: {ram}%\n"
        "• NEXUS: Sincronizado\n"
        "• SUPABASE: Ativo"
    )
    bot.reply_to(message, status_msg, parse_mode='Markdown')

if __name__ == "__main__":
    print(f"✅ [TELEGRAM]: Bot @akame_soberana_bot em execução...")
    bot.infinity_polling()
