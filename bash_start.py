#!/bin/bash

echo "🚀 Memulai semua script Python 3.11..."

# Cek apakah Python 3.11 tersedia
if ! command -v python3.11 &> /dev/null
then
    echo "❌ Python 3.11 tidak ditemukan. Pastikan sudah terinstal!"
    exit 1
fi

# Aktivasi virtual environment (jika ada)
if [ -d "venv" ]; then
    echo "🔄 Mengaktifkan virtual environment..."
    source venv/bin/activate
fi

# Install dependencies jika belum ada
echo "📦 Memeriksa dan menginstal dependencies..."
pip install -r requirements.txt

# Jalankan semua script Python di background
echo "⚡ Menjalankan bot dan analisis trading..."
python3.11 main.py & 
python3.11 forex_factory.py & 
python3.11 scalping.py & 
python3.11 auto_trading.py & 

echo "✅ Semua script berjalan di background!"
echo
