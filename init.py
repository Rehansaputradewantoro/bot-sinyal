# __init__.py

import os
import logging
from dotenv import load_dotenv

# Memuat variabel dari file .env
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
OWNER_ID = os.getenv("OWNER_ID")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
MONGO_URI = os.getenv("MONGO_URI")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

init.py

import os import logging from dotenv import load_dotenv

Memuat variabel dari file .env

load_dotenv()

Konfigurasi logging

logging.basicConfig(level=logging.INFO) logger = logging.getLogger(name)

Variabel lingkungan

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") API_ID = os.getenv("API_ID") API_HASH = os.getenv("API_HASH") MONGO_URI = os.getenv("MONGO_URI")

logger.info("Modul diinisialisasi dengan sukses.")

