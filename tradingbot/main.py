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
