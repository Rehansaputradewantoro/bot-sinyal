from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext

# Fungsi untuk menangani pesan teks
def handle_text(update: Update, context: CallbackContext):
    """Menangani semua pesan teks dan memberikan respons otomatis."""
    user_text = update.message.text.lower()
    
    if "hello" in user_text or "hi" in user_text:
        response = "👋 Hai! Bagaimana saya bisa membantu Anda?"
    elif "otp" in user_text:
        response = "🔐 Gunakan perintah /otp untuk mendapatkan kode OTP verifikasi."
    elif "price" in user_text:
        response = "💰 Gunakan perintah /price <symbol> untuk melihat harga terbaru."
    else:
        response = "⚡ Maaf, saya tidak mengerti. Gunakan /help untuk melihat perintah yang tersedia."

    update.message.reply_text(response)

# Fungsi untuk daftar perintah yang tersedia
def help_command(update: Update, context: CallbackContext):
    help_text = """
🛠 **Perintah yang Tersedia**:
- `/start` : Mulai bot
- `/otp` : Dapatkan kode OTP
- `/price <symbol>` : Cek harga aset
- `/help` : Lihat semua perintah
    """
    update.message.reply_text(help_text)

# Fungsi untuk menghubungkan `text.py` ke `main.py`
def add_text_handlers(dispatcher):
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))
    dispatcher.add_handler(CommandHandler("help", help_command))
