# mt5_connector.py
import MetaTrader5 as mt5
from config import BROKERS, SELECTED_BROKER

def connect_mt5():
    broker = BROKERS[SELECTED_BROKER]
    
    if not mt5.initialize(login=broker["login"], password=broker["password"], server=broker["server"]):
        print(f"❌ Gagal terhubung ke {SELECTED_BROKER}")
        mt5.shutdown()
        return False
    
    print(f"✅ Berhasil terhubung ke {SELECTED_BROKER}")
    return True
