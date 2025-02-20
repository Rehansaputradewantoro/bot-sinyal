import random
import time
import logging
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Konfigurasi bot Telegram
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Simpan OTP sementara
otp_storage = {}

def send_otp(update: Update, context: CallbackContext):
    """Mengirim OTP ke pengguna Telegram."""
    chat_id = update.message.chat_id
    otp = str(random.randint(100000, 999999))  # OTP 6 digit
    otp_storage[chat_id] = otp

    bot.send_message(chat_id=chat_id, text=f"🔐 Kode OTP Anda: {otp}. Berlaku selama 5 menit.")
    update.message.reply_text("✅ OTP telah dikirim ke Telegram Anda. Silakan masukkan kode untuk verifikasi.")

def verify_otp(update: Update, context: CallbackContext):
    """Memverifikasi OTP yang dikirim oleh pengguna."""
    chat_id = update.message.chat_id
    user_input = update.message.text.strip()

    if chat_id in otp_storage and otp_storage[chat_id] == user_input:
        del otp_storage[chat_id]  # Hapus OTP setelah digunakan
        update.message.reply_text("✅ Login berhasil! Anda telah terverifikasi.")
    else:
        update.message.reply
