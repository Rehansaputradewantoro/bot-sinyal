#!/bin/bash

Aktivasi virtual environment (opsional, jika digunakan)

source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Jalankan bot

python bot.py

chmod +x start_bot.sh  # Memberikan izin eksekusi
./start_bot.sh

  import subprocess
import time
import logging

# Logging untuk melihat status bot
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Fungsi untuk menjalankan script utama
def start_bot():
    try:
        logging.info("🚀 Memulai bot trading dan Telegram...")
        processes = [
            subprocess.Popen(["python", "main.py"]),       # Jalankan bot utama
            subprocess.Popen(["python", "scalping.py"]),   # Jalankan strategi scalping
            subprocess.Popen(["python", "broadcast.py"]),  # Jalankan fitur broadcast pesan
            subprocess.Popen(["python", "payment.py"]),    # Jalankan fitur pembayaran
        ]
        
        # Tunggu proses berjalan
        for process in processes:
            process.wait()
    
    except Exception as e:
        logging.error(f"❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    start_bot()
