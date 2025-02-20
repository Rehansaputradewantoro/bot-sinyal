import ccxt import requests import time import MetaTrader5 as mt5 import pymongo from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

Konfigurasi API Telegram

TELEGRAM_BOT_TOKEN = "your_telegram_bot_token" TELEGRAM_CHAT_ID = "your_channel_or_chat_id" OWNER_ID = "your_owner_id" API_ID = "your_api_id" API_HASH = "your_api_hash"

Konfigurasi MongoDB

MONGO_URI = "your_mongodb_uri" client = pymongo.MongoClient(MONGO_URI) db = client.get_database("trading_bot_db")

Konfigurasi MT5 untuk berbagai broker

BROKERS = { "Exness": {"login": 12345678, "password": "your_mt5_password", "server": "Exness-MT5Real"}, "ICMarkets": {"login": 87654321, "password": "your_mt5_password", "server": "ICMarkets-MT5"}, "ForexCom": {"login": 11223344, "password": "your_mt5_password", "server": "ForexCom-MT5"} }

SELECTED_BROKER = "Exness" MT5_LOGIN = BROKERS[SELECTED_BROKER]["login"] MT5_PASSWORD = BROKERS[SELECTED_BROKER]["password"] MT5_SERVER = BROKERS[SELECTED_BROKER]["server"]

bot = Bot(token=TELEGRAM_BOT_TOKEN)

Fungsi untuk mengirim pesan ke Telegram

def send_telegram_message(message, buttons=None): if buttons: reply_markup = InlineKeyboardMarkup(buttons) else: reply_markup = None bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message, reply_markup=reply_markup)

Fungsi untuk menangani tombol perintah

def button_handler(update, context): query = update.callback_query query.answer() command = query.data if command == "buy": message = "📈 Membuka posisi BUY" elif command == "sell": message = "📉 Membuka posisi SELL" elif command == "owner": message = f"👑 Owner ID: {OWNER_ID}" elif command == "payment": message = "💳 Silakan lakukan pembayaran di sini: your_payment_link" else: message = "Perintah tidak dikenal." send_telegram_message(message)

Inisialisasi exchange (misal, Binance atau broker lain yang didukung CCXT)

exchange = ccxt.binance()

Fungsi untuk mendapatkan harga terbaru

def get_latest_price(symbol): ticker = exchange.fetch_ticker(symbol) return ticker['last']

Fungsi untuk koneksi ke MT5

def connect_mt5(): if not mt5.initialize(login=MT5_LOGIN, password=MT5_PASSWORD, server=MT5_SERVER): print(f"Gagal menghubungkan ke {SELECTED_BROKER} di MetaTrader 5") mt5.shutdown() else: print(f"Berhasil terhubung ke {SELECTED_BROKER} di MetaTrader 5")

Daftar simbol pair crypto, forex, stocks, dan XAU/USD

SYMBOLS = [ "BTC/USDT", "ETH/USDT", "XRP/USDT", "LTC/USDT", "ADA/USDT",  # Crypto pairs "EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", "USD/CAD", "USD/CHF",  # Forex pairs "AAPL", "TSLA", "GOOGL", "MSFT", "AMZN",  # Stock symbols "XAU/USD"  # Gold (XAU/USD) ] INTERVAL = 60  # detik

connect_mt5() updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True) dp = updater.dispatcher dp.add_handler(CallbackQueryHandler(button_handler)) updater.start_polling()

while True: for symbol in SYMBOLS: price = get_latest_price(symbol) buttons = [[InlineKeyboardButton("BUY", callback_data="buy"), InlineKeyboardButton("SELL", callback_data="sell")], [InlineKeyboardButton("OWNER", callback_data="owner"), InlineKeyboardButton("PAYMENT", callback_data="payment")]] send_telegram_message(f"📊 Sinyal trading untuk {symbol}: {price}", buttons) time.sleep(INTERVAL)

