from telegram import Update from telegram.ext import Updater, CommandHandler, CallbackContext from buttons import get_main_menu from gban import gban, ungban from absen import absen, cek_absen from broadcast import broadcast_message

Token bot Telegram

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

def start(update: Update, context: CallbackContext): update.message.reply_text("Welcome to the bot!", reply_markup=get_main_menu())

def main(): updater = Updater(TOKEN, use_context=True) dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("gban", gban))
dp.add_handler(CommandHandler("ungban", ungban))
dp.add_handler(CommandHandler("absen", absen))
dp.add_handler(CommandHandler("cek_absen", cek_absen))

updater.start_polling()
updater.idle()

if name == "main": main()

from telegram.ext import Updater
from text import add_text_handlers  # Import dari text.py

TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"

def main():
    updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Tambahkan handler dari text.py
    add_text_handlers(dp)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

from telegram.ext import Updater
from text import add_text_handlers
from buttons import add_button_handlers
from broadcast import add_broadcast_handlers
from gban import add_gban_handlers

TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"

def main():
    updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Tambahkan handler dari semua script
    add_text_handlers(dp)
    add_button_handlers(dp)
    add_broadcast_handlers(dp)
    add_gban_handlers(dp)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
from scalping import scalping

def button_handler(update, context):
    query = update.callback_query
    query.answer()
    command = query.data

    if command == "start_scalping":
        send_telegram_message("🚀 Memulai scalping otomatis...")
        scalping()
    elif command == "stop_scalping":
        send_telegram_message("⛔ Scalping dihentikan.")

from market_hours import get_market_status
from telegram import Bot

# Konfigurasi bot Telegram
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
bot = Bot(token=TELEGRAM_BOT_TOKEN)

def send_market_hours():
    """Mengirim info jam pasar ke Telegram"""
    market_status = get_market_status()
    message = "📊 **Jam Pasar Forex Saat Ini:**\n"
    for market, status in market_status.items():
        message += f"✅ {market}: {status}\n"

    bot.send_message(chat_id="your_chat_id", text=message)

# Kirim info pasar saat bot aktif
send_market_hours()

from forex_factory import send_forex_news

def send_market_analysis():
    """Mengirim analisa forex secara otomatis."""
    send_forex_news()

# Kirim info analisa saat bot aktif
send_market_analysis()
