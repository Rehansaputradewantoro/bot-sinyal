import os import logging from dotenv import load_dotenv from bot import start_bot

Memuat variabel dari file .env

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID") OWNER_ID = os.getenv("OWNER_ID") API_ID = os.getenv("API_ID") API_HASH = os.getenv("API_HASH") MONGO_URI = os.getenv("MONGO_URI")

logging.basicConfig(level=logging.INFO) logger = logging.getLogger(name)

def main(): logger.info("Memulai bot...") start_bot()

if name == "main": main()

import logging from bot import start_bot

Konfigurasi logging

logging.basicConfig(level=logging.INFO) logger = logging.getLogger(name)

def main(): logger.info("Memulai bot...") start_bot()

if name == "main": main()

# main.py

import sys

# Pastikan script berjalan di Python 3.11
REQUIRED_PYTHON = (3, 11)
if sys.version_info[:2] != REQUIRED_PYTHON:
    sys.exit(f"Error: Script ini membutuhkan Python {REQUIRED_PYTHON[0]}.{REQUIRED_PYTHON[1]}!")

import logging

# Konfigurasi logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Script berjalan di Python 3.11 dengan sukses!")

if __name__ == "__main__":
    main()
