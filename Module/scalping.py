import MetaTrader5 as mt5
import time
import pandas as pd
import numpy as np

# Koneksi ke MetaTrader 5
from trading import connect_mt5, get_price, place_trade
from main import send_telegram_message

# Pilihan Akun Exness (Real & Demo)
SELECTED_BROKER = "Exness-Real1"

# Daftar simbol yang dipantau
SYMBOLS = ["XAUUSD", "EURUSD", "GBPUSD", "USDJPY"]
TIMEFRAME = mt5.TIMEFRAME_M1  # Scalping di timeframe 1 menit
TRADE_VOLUME = 0.1  # Lot size
RSI_PERIOD = 14
MA_PERIOD = 50

# Fungsi untuk mendapatkan data harga (candlestick)
def get_candles(symbol, timeframe, num_candles=100):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, num_candles)
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

# Fungsi untuk menghitung indikator RSI
def calculate_rsi(df, period=14):
    delta = df['close'].diff()
    gain = np.where(delta > 0, delta, 0)
    loss = np.where(delta < 0, -delta, 0)
    
    avg_gain = pd.Series(gain).rolling(window=period).mean()
    avg_loss = pd.Series(loss).rolling(window=period).mean()
    
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))
    return df

# Fungsi untuk menghitung Moving Average
def calculate_ma(df, period=50):
    df['MA'] = df['close'].rolling(window=period).mean()
    return df

# Fungsi untuk menentukan sinyal beli atau jual
def generate_signal(symbol):
    df = get_candles(symbol, TIMEFRAME)
    df = calculate_rsi(df, RSI_PERIOD)
    df = calculate_ma(df, MA_PERIOD)

    last_rsi = df['RSI'].iloc[-1]
    last_price = df['close'].iloc[-1]
    last_ma = df['MA'].iloc[-1]

    if last_rsi < 30 and last_price > last_ma:
        return "buy"
    elif last_rsi > 70 and last_price < last_ma:
        return "sell"
    return None

# Fungsi utama untuk scalping
[[InlineKeyboardButton("⚡ Mulai Scalping", callback_data="start_scalping"),
  InlineKeyboardButton("⛔ Stop Scalping", callback_data="stop_scalping")]]
