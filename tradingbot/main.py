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
