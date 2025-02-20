import os import logging from dotenv import load_dotenv from bot import start_bot
import time
from mt5_login import connect_mt5, get_account_info
from telegram_bot import send_telegram_message
from database import save_trade

SYMBOLS = ["XAU/USD", "EUR/USD", "BTC/USDT"]  # Daftar simbol trading
INTERVAL = 60  # Waktu update dalam detik

if __name__ == "__main__":
    if connect_mt5():
        send_telegram_message("✅ Bot trading telah dimulai!")
        
        while True:
            account_info = get_account_info()
            if account_info:
                message = f"💰 Balance: {account_info['balance']}\n📊 Equity: {account_info['equity']}\n📈 Free Margin: {account_info['margin_free']}"
                send_telegram_message(message)
                save_trade(account_info)
            
            time.sleep(INTERVAL)

Memuat variabel dari file .env

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID") OWNER_ID = os.getenv("OWNER_ID") API_ID = os.getenv("API_ID") API_HASH = os.getenv("API_HASH") MONGO_URI = os.getenv("MONGO_URI")

logging.basicConfig(level=logging.INFO) logger = logging.getLogger(name)

def main(): logger.info("Memulai bot...") start_bot()

if name == "main": main()

import logging from bot import start_bot

Konfigurasi logging

logging.basicConfig(level=logging.INFO) logger = logging.getLogger(name)

def main(): logger.info("Memulai bot...") start_bot()

if name == "main": main()

# main.py

import sys

# Pastikan script berjalan di Python 3.11
REQUIRED_PYTHON = (3, 11)
if sys.version_info[:2] != REQUIRED_PYTHON:
    sys.exit(f"Error: Script ini membutuhkan Python {REQUIRED_PYTHON[0]}.{REQUIRED_PYTHON[1]}!")

import logging

# Konfigurasi logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Script berjalan di Python 3.11 dengan sukses!")

if __name__ == "__main__":
    main()
