import MetaTrader5 as mt5
import time

# Konfigurasi Akun Exness (Semua Server)
BROKERS = {
    "Exness-Real1": {"login": 12345678, "password": "your_real_password", "server": "Exness-MT5Real"},
    "Exness-Real2": {"login": 22334455, "password": "your_real_password", "server": "Exness-MT5Real2"},
    "Exness-Demo1": {"login": 87654321, "password": "your_demo_password", "server": "Exness-MT5Demo"},
    "Exness-Demo2": {"login": 55667788, "password": "your_demo_password", "server": "Exness-MT5Demo2"},
}

# Pilih akun yang ingin digunakan
SELECTED_BROKER = "Exness-Real1"  # Ganti ke akun lain jika perlu
MT5_LOGIN = BROKERS[SELECTED_BROKER]["login"]
MT5_PASSWORD = BROKERS[SELECTED_BROKER]["password"]
MT5_SERVER = BROKERS[SELECTED_BROKER]["server"]

# Koneksi ke MetaTrader 5
def connect_mt5():
    if not mt5.initialize(login=MT5_LOGIN, password=MT5_PASSWORD, server=MT5_SERVER):
        print(f"❌ Gagal terhubung ke {SELECTED_BROKER}")
        return False
    print(f"✅ Terhubung ke {SELECTED_BROKER}")
    return True

# Fungsi untuk mendapatkan harga saat ini
def get_price(symbol):
    tick = mt5.symbol_info_tick(symbol)
    return tick.bid, tick.ask

# Fungsi untuk menentukan SL & TP otomatis
def calculate_sl_tp(price, trade_type, sl_pips=50, tp_pips=100):
    point = mt5.symbol_info(symbol).point
    if trade_type == "buy":
        sl = price - sl_pips * point
        tp = price + tp_pips * point
    else:
        sl = price + sl_pips * point
        tp = price - tp_pips * point
    return sl, tp

# Fungsi untuk membuka posisi trading otomatis
def place_trade(symbol, volume, trade_type):
    price = get_price(symbol)[1] if trade_type == "buy" else get_price(symbol)[0]
    sl, tp = calculate_sl_tp(price, trade_type)

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": mt5.ORDER_TYPE_BUY if trade_type == "buy" else mt5.ORDER_TYPE_SELL,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": 10,
        "magic": 123456,
        "comment": "Auto Trade with SL & TP",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)
    if result.retcode == mt5.TRADE_RETCODE_DONE:
        print(f"✅ Order {trade_type.upper()} berhasil di {symbol} dengan SL {sl} & TP {tp}")
    else:
        print(f"❌ Gagal melakukan order {trade_type.upper()} untuk {symbol}: {result.comment}")

# Auto Trading Loop
SYMBOLS = ["XAUUSD", "EURUSD", "GBPUSD"]
TRADE_VOLUME = 0.1  # Lot size
INTERVAL = 60  # Waktu antar order dalam detik

def auto_trade():
    if not connect_mt5():
        return
    
    while True:
        for symbol in SYMBOLS:
            print(f"📊 Trading otomatis untuk {symbol}")
            place_trade(symbol, TRADE_VOLUME, "buy")  # Auto BUY
            place_trade(symbol, TRADE_VOLUME, "sell")  # Auto SELL
            time.sleep(INTERVAL)
