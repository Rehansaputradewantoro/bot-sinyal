import requests
from telegram import Bot

# Konfigurasi API Telegram
TELEGRAM_BOT_TOKEN = "your_telegram_bot_token"
TELEGRAM_CHAT_ID = "your_channel_or_chat_id"
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Contoh API pembayaran (Stripe, Midtrans, PayPal, dll.)
PAYMENT_API_URL = "https://api.example.com/payments"
PAYMENT_API_KEY = "your_payment_api_key"

def process_payment(user_id, amount, payment_method):
    """Mengirim permintaan pembayaran ke API dan mengirim notifikasi."""
    data = {
        "user_id": user_id,
        "amount": amount,
        "method": payment_method
    }
    
    response = requests.post(PAYMENT_API_URL, json=data, headers={"Authorization": f"Bearer {PAYMENT_API_KEY}"})
    
    if response.status_code == 200:
        send_payment_notification(user_id, amount, payment_method)
        return True
    else:
        return False

def send_payment_notification(user_id, amount, payment_method):
    """Mengirim notifikasi pembayaran ke Telegram."""
    message = f"✅ Pembayaran berhasil!\n👤 User: {user_id}\n💰 Jumlah: {amount}\n💳 Metode: {payment_method}"
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
