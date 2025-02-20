# config.py
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
TELEGRAM_CHAT_ID = "your_channel_or_chat_id"

# Konfigurasi MetaTrader 5 untuk Exness
BROKERS = {
    "Exness-Real": {
        "login": 12345678,
        "password": "your_real_password",
        "server": "Exness-MT5Real"
    },
    "Exness-Demo": {
        "login": 87654321,
        "password": "your_demo_password",
        "server": "Exness-MT5Trial"
    }
}

SELECTED_BROKER = "Exness-Real"  # Ganti ke "Exness-Demo" jika ingin login ke akun demo
