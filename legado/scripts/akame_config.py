# 🔱 AKAME CORE CONFIGURATION - SOBERANIA TOTAL
import os

# Os tokens são injetados via Vault (os.environ) para segurança
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "PROTECTED")
HF_TOKEN = os.getenv("HF_TOKEN", "PROTECTED")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "PROTECTED")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "PROTECTED")

print("🔱 [CONFIG]: Variáveis de ambiente carregadas via Vault.")
