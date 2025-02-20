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

import openai
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackContext

# Konfigurasi OpenAI API (Masukkan API Key Anda)
OPENAI_API_KEY = "your_openai_api_key"
openai.api_key = OPENAI_API_KEY

def handle_text(update: Update, context: CallbackContext):
    """Menangani semua pesan teks dan memberikan respons AI otomatis."""
    user_text = update.message.text

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_text}]
        )
        ai_reply = response["choices"][0]["message"]["content"]

    except Exception:
        ai_reply = "⚠️ Maaf, saya mengalami kesalahan saat memproses permintaan Anda."

    update.message.reply_text(ai_reply)

def help_command(update: Update, context: CallbackContext):
    help_text = """
🛠 **Perintah Tersedia**:
- `/start` : Mulai bot
- `/help` : Lihat semua perintah
- **Chat AI**: Ketik apa saja untuk mendapatkan jawaban AI
    """
    update.message.reply_text(help_text)

def add_text_handlers(dispatcher):
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))
    dispatcher.add_handler(CommandHandler("help", help_command))
