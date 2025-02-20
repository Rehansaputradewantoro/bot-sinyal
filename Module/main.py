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
