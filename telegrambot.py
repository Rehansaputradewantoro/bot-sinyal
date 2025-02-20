from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

bot = Bot(token=TELEGRAM_BOT_TOKEN)

def send_telegram_message(message, buttons=None):
    """Mengirim pesan ke Telegram dengan tombol"""
    if buttons:
        reply_markup = InlineKeyboardMarkup(buttons)
    else:
        reply_markup = None

    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message, reply_markup=reply_markup)
