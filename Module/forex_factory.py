import requests
from bs4 import BeautifulSoup
from telegram import Bot

# Konfigurasi bot Telegram
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
TELEGRAM_CHAT_ID = "your_chat_id"
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# URL Forex Factory (Kalender Ekonomi)
FOREX_FACTORY_URL = "https://www.forexfactory.com/calendar"

def get_forex_news():
    """Scrape data berita ekonomi dari Forex Factory dan analisa sentimen positif/negatif."""
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(FOREX_FACTORY_URL, headers=headers)

    if response.status_code != 200:
        return "⚠️ Gagal mengambil data dari Forex Factory."

    soup = BeautifulSoup(response.text, "html.parser")
    news_items = soup.find_all("tr
