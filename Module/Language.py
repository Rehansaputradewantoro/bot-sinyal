language.py

class Language: LANGUAGES = { "en": { "welcome": "Welcome to the trading bot!", "error": "An error occurred!", "connected": "Successfully connected to MetaTrader 5!", "trade_signal": "New trade signal: {pair} at {price}", }, "id": { "welcome": "Selamat datang di bot trading!", "error": "Terjadi kesalahan!", "connected": "Berhasil terhubung ke MetaTrader 5!", "trade_signal": "Sinyal perdagangan baru: {pair} di {price}", }, }

def __init__(self, lang="en"):
    self.lang = lang if lang in self.LANGUAGES else "en"

def get(self, key, **kwargs):
    """Retrieve translated message with optional formatting."""
    message = self.LANGUAGES[self.lang].get(key, "Message not found")
    return message.format(**kwargs) if "{" in message else message

Example usage:

if name == "main": lang = Language("id") print(lang.get("welcome"))  # Output: Selamat datang di bot trading! print(lang.get("trade_signal", pair="EUR/USD", price="1.2345"))

