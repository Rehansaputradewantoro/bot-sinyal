# main.py
import time
from mt5_connector import connect_mt5
from telegram_bot import send_telegram_message

def main():
    if connect_mt5():
        send_telegram_message("✅ Bot Trading Terhubung ke MetaTrader 5!")
        
        while True:
            send_telegram_message("📊 Cek sinyal trading...")
            time.sleep(60)  # Tunggu 60 detik sebelum update harga berikutnya

if __name__ == "__main__":
    main()

from payment import process_payment

def handle_payment():
    user_id = input("Masukkan ID pengguna: ")
    amount = float(input("Masukkan jumlah pembayaran: "))
    method = input("Pilih metode pembayaran (Transfer/QRIS/PayPal): ")
    
    if process_payment(user_id, amount, method):
        print("✅ Pembayaran berhasil!")
    else:
        print("❌ Pembayaran gagal, coba lagi.")

handle_payment()

from trading import auto_trade
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Konfigurasi Telegram
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
TELEGRAM_CHAT_ID = "your_chat_id"
OWNER_ID = "your_owner_id"

bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Fungsi untuk mengirim pesan ke Telegram
def send_telegram_message(message, buttons=None):
    if buttons:
        reply_markup = InlineKeyboardMarkup(buttons)
    else:
        reply_markup = None
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message, reply_markup=reply_markup)

# Fungsi untuk menangani tombol perintah di Telegram
def button_handler(update, context):
    query = update.callback_query
    query.answer()
    command = query.data

    if command == "start_trading":
        send_telegram_message("🔄 Memulai trading otomatis...")
        auto_trade()
    elif command == "stop_trading":
        send_telegram_message("⛔ Trading dihentikan.")
    else:
        send_telegram_message("❌ Perintah tidak dikenal.")

# Konfigurasi Bot Telegram
updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CallbackQueryHandler(button_handler))

# Menjalankan Bot
send_telegram_message("🤖 Bot siap! Gunakan tombol untuk mengontrol trading.", 
                      [[InlineKeyboardButton("▶️ Mulai Trading", callback_data="start_trading"),
                        InlineKeyboardButton("⛔ Stop Trading", callback_data="stop_trading")]])

updater.start_polling()
