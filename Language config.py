import os from dotenv import load_dotenv

Memuat variabel dari file .env

load_dotenv()

LANGUAGE = os.getenv("LANGUAGE", "en")

Dictionary untuk bahasa yang didukung

LANGUAGES = { "en": { "start": "Bot started successfully!", "error": "An error occurred.", "buy": "Buying asset...", "sell": "Selling asset..." }, "id": { "start": "Bot berhasil dimulai!", "error": "Terjadi kesalahan.", "buy": "Membeli aset...", "sell": "Menjual aset..." } }

def get_message(key): return LANGUAGES.get(LANGUAGE, LANGUAGES["en"]).get(key, "Message not found")

if name == "main": print(get_message("start"))

