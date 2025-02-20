import ccxt
import requests
import time
import pymongo

from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

from config import (
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID,
    OWNER_ID,
    API_ID,
    API_HASH,
    MONGO_URI,
)
from config import SELECTED_BROKER
print(SELECTED_BROKER)

# Koneksi ke MongoDB
from pymongo import MongoClient

client = MongoClient(MONGO_URI)  # Gunakan MONGO_URI yang sudah di-import
db = client["nama_database"]  # Ganti dengan nama database yang sesuai

client = pymongo.MongoClient(MONGO_URI); db = client.get_database("trading_bot_db")

""" Konfigurasi MT5 """

from config import BROKERS, SELECTED_BROKER  # Impor bersamaan

MT5_LOGIN = BROKERS[SELECTED_BROKER]["login"]
MT5_PASSWORD = BROKERS[SELECTED_BROKER]["password"]
MT5_SERVER = BROKERS[SELECTED_BROKER]["server"]

def connect_mt5():
    if not mt5.initialize(login=MT5_LOGIN, password=MT5_PASSWORD, server=MT5_SERVER):
        print(f"Gagal menghubungkan ke {SELECTED_BROKER} di MetaTrader 5")
        mt5.shutdown()
    else:
        print(f"Berhasil terhubung ke {SELECTED_BROKER} di MetaTrader 5")

# Inisialisasi bot Telegram

bot = Bot(token=TELEGRAM_BOT_TOKEN)

def send_telegram_message(message, buttons=None):  
    reply_markup = InlineKeyboardMarkup(buttons) if buttons else None  
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message, reply_markup=reply_markup)

def button_handler(update, context):  
    query = update.callback_query  
    query.answer()  
    command = query.data  

    messages = {  
        "buy": "📈 Membuka posisi BUY",  
        "sell": "📉 Membuka posisi SELL",  
        "owner": f"👑 Owner ID: {OWNER_ID}",  
        "payment": "💳 Silakan lakukan pembayaran di sini: your_payment_link"  
    }  

    send_telegram_message(messages.get(command, "Perintah tidak dikenal."))

# Inisialisasi CCXT

exchange = ccxt.binance()

def get_latest_price(symbol):  
    ticker = exchange.fetch_ticker(symbol)  
    return ticker['last']

# Daftar simbol trading

SYMBOLS = [
    # Crypto pairs
    "BTC/USDT", "ETH/USDT", "XRP/USDT", "LTC/USDT", "ADA/USDT",

    # Forex pairs
    "EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CAD", "USD/CHF",

    # Stock symbols
    "AAPL", "TSLA", "GOOGL", "MSFT", "AMZN",

    # Gold
    "XAU/USD"
]

INTERVAL = 60  # detik

connect_mt5()

updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CallbackQueryHandler(button_handler))

updater.start_polling()

while True:
    for symbol in SYMBOLS:
        price = get_latest_price(symbol)

        buttons = [
            [InlineKeyboardButton("BUY", callback_data="buy"), InlineKeyboardButton("SELL", callback_data="sell")], 
            [InlineKeyboardButton("OWNER", callback_data="owner"), InlineKeyboardButton("PAYMENT", callback_data="payment")]
        ] 
        
        send_telegram_message(f"📊 Sinyal trading untuk {symbol}: {price}", buttons)

        time.sleep(INTERVAL)

import os 
import ccxt 
import time
import requests
import pymongo as mt5 
import pymongo
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Import semua modul yang ada dalam proyek

from .config import (
    TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, OWNER_ID, 
    API_ID, API_HASH, MONGO_URI, BROKERS, SELECTED_BROKER
)
from .buttons import button_handler
from .helpers import send_telegram_message, get_latest_price, connect_mt5
from .broadcast import broadcast_message
from .gban import global_ban

# Inisialisasi MongoDB

client = pymongo.MongoClient(MONGO_URI); db = client.get_database("trading_bot_db")

# Inisialisasi bot Telegram

bot = Bot(token=TELEGRAM_BOT_TOKEN); updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True); dp = updater.dispatcher; dp.add_handler(CallbackQueryHandler(button_handler))

# Koneksi ke MetaTrader 5

connect_mt5()

# Mulai bot Telegram

updater.start_polling()

print("Bot trading telah berjalan dengan sukses!")

