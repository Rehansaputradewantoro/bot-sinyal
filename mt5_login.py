import MetaTrader5 as mt5
from config import MT5_LOGIN, MT5_PASSWORD, MT5_SERVER

def connect_mt5():
    """Fungsi untuk menghubungkan ke MetaTrader 5"""
    if not mt5.initialize(login=MT5_LOGIN, password=MT5_PASSWORD, server=MT5_SERVER):
        print(f"❌ Gagal menghubungkan ke MetaTrader 5: {mt5.last_error()}")
        return False
    print("✅ Berhasil terhubung ke MetaTrader 5!")
    return True

def get_account_info():
    """Mendapatkan informasi akun trading"""
    if not mt5.login(MT5_LOGIN, MT5_PASSWORD, MT5_SERVER):
        print(f"❌ Gagal login: {mt5.last_error()}")
        return None
    
    account_info = mt5.account_info()
    if account_info:
        return {
            "balance": account_info.balance,
            "equity": account_info.equity,
            "margin_free": account_info.margin_free
        }
    return None

if __name__ == "__main__":
    if connect_mt5():
        print(get_account_info())
    mt5.shutdown()
