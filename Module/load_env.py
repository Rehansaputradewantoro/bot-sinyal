import os
from dotenv import load_dotenv

# Memuat variabel dari file sample.env
load_dotenv("sample.env")

# Mengambil variabel yang telah dimuat
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
OWNER_ID = os.getenv("OWNER_ID")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
MONGO_URI = os.getenv("MONGO_URI")
MT5_LOGIN = os.getenv("MT5_LOGIN")
MT5_PASSWORD = os.getenv("MT5_PASSWORD")
MT5_SERVER = os.getenv("MT5_SERVER")

# Menampilkan variabel untuk verifikasi (opsional)
print(f"🔹 TELEGRAM_BOT_TOKEN: {TELEGRAM_BOT_TOKEN}")
print(f"🔹 TELEGRAM_CHAT_ID: {TELEGRAM_CHAT_ID}")
print(f"🔹 OWNER_ID: {OWNER_ID}")
print(f"🔹 API_ID: {API_ID}")
print(f"🔹 API_HASH: {API_HASH}")
print(f"🔹 MONGO_URI: {MONGO_URI}")
print(f"🔹 MT5_LOGIN: {MT5_LOGIN}")
print(f"🔹 MT5_SERVER: {MT5_SERVER}")
