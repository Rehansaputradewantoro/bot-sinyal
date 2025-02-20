from datetime import datetime
import pytz
import time
from telegram import Bot

# Konfigurasi bot Telegram
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
TELEGRAM_CHAT_ID = "your_chat_id"
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Zona waktu utama untuk pasar forex
MARKET_ZONES = {
    "Asia (Tokyo)": "Asia/Tokyo",
    "London (UK)": "Europe/London",
    "New York (US)": "America/New_York"
}

# Waktu buka dan tutup pasar (GMT)
MARKET_HOURS = {
    "Asia (Tokyo)": {"open": 0, "close": 9},      # 00:00 - 09:00 GMT
    "London (UK)": {"open": 8, "close": 17},      # 08:00 - 17:00 GMT
    "New York (US
