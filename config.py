# Konfigurasi Telegram
TELEGRAM_BOT_TOKEN = "7877517758:AAHm0ZdmAj3dHxqbPMmz9AyhqkstVu9K4no"
TELEGRAM_CHAT_ID = "-1002451875261"
OWNER_ID = "8071717425"
API_ID = "24888690"
API_HASH = "15d9737a0ebdf38c7244b2b04b3efb50"

# Konfigurasi MongoDB
MONGO_URI = "your_mongodb_uri"
DATABASE_NAME = "trading_bot_db"

# Konfigurasi Akun MetaTrader 5
MT5_LOGIN = 12345678  # Ganti dengan login akun MT5 Anda
MT5_PASSWORD = "your_mt5_password"  # Ganti dengan password akun MT5 Anda
MT5_SERVER = "Exness-MT5Real"  # Ganti dengan server broker Anda

SELECTED_BROKER = "broker1"  # Pastikan ini ada di dalam file

BROKERS = {
    "broker1": {
        "login": "123456",
        "password": "password123",
        "server": "broker1-server"
    },
    "broker2": {
        "login": "654321",
        "password": "password456",
        "server": "broker2-server"
    }
}

BROKERS = {
    "broker1": {
        "login": "123456",
        "password": "password123",
        "server": "broker1-server"
    },
    "broker2": {
        "login": "654321",
        "password": "password456",
        "server": "broker2-server"
    }
}

# Daftar simbol trading
SYMBOLS = ["XAUUSD", "EURUSD", "BTCUSD"]

# Lot size default
LOT_SIZE = 0.10
