from telegram import Bot
import asyncio

# Masukkan BOT TOKEN Anda
BOT_TOKEN = "your_telegram_bot_token"

# Daftar grup atau channel yang ingin dijoin
GROUPS_TO_JOIN = [
    "@example_group1",  # Ganti dengan username grup/channel
    "@example_group2"
]

async def auto_join_groups():
    bot = Bot(token=BOT_TOKEN)
    for group in GROUPS_TO_JOIN:
        try:
            await bot.join_chat(group)
            print(f"✅ Berhasil join ke: {group}")
        except Exception as e:
            print(f"❌ Gagal join ke {group}: {e}")

# Jalankan fungsi
asyncio.run(auto_join_groups())
