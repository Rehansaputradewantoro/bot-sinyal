import MetaTrader5 as mt5 import logging import time import requests from telegram import Bot from dotenv import load_dotenv import os

Load environment variables

load_dotenv() TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID") MT5_LOGIN = int(os.getenv("MT5_LOGIN")) MT5_PASSWORD = os.getenv("MT5_PASSWORD") MT5_SERVER = os.getenv("MT5_SERVER")

Initialize logging

logging.basicConfig(level=logging.INFO) logger = logging.getLogger(name)

Initialize Telegram bot

bot = Bot(token=TELEGRAM_BOT_TOKEN)

def send_telegram_message(message: str): """Send message to Telegram channel.""" bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

def connect_mt5(): """Connect to MetaTrader 5.""" if not mt5.initialize(): logger.error("Failed to initialize MT5") return False

authorized = mt5.login(MT5_LOGIN, password=MT5_PASSWORD, server=MT5_SERVER)
if not authorized:
    logger.error("Failed to log in to MT5")
    return False

logger.info("Connected to MT5 successfully")
return True

def check_market(): """Check market conditions and send signals.""" symbols = ["EURUSD", "GBPUSD", "XAUUSD"]  # List of trading pairs

for symbol in symbols:
    info = mt5.symbol_info_tick(symbol)
    if info:
        message = f"{symbol} Price: {info.bid}"
        send_telegram_message(message)
        logger.info(message)

def main(): """Main function to run the bot.""" if not connect_mt5(): return

while True:
    check_market()
    time.sleep(60)  # Check market every minute

if name == "main": main()

