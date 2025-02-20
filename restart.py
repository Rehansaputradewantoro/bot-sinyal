import os
import sys
import time

def restart_bot():
    print("♻️ Memulai ulang bot...")
    time.sleep(2)  # Tunggu sebentar sebelum restart
    os.execv(sys.executable, ['python3.11'] + sys.argv)

if __name__ == "__main__":
    print("🔄 Restarting bot...")
    restart_bot()
