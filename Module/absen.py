from telegram import Update from telegram.ext import CallbackContext, CommandHandler, Updater

Simpan daftar pengguna yang tidak aktif

inactive_users = {}

def absen(update: Update, context: CallbackContext): user_id = update.message.from_user.id username = update.message.from_user.username or user_id

inactive_users[user_id] = username
update.message.reply_text(f"{username} telah ditandai sebagai tidak aktif.")

def cek_absen(update: Update, context: CallbackContext): if not inactive_users: update.message.reply_text("Tidak ada pengguna yang tidak aktif.") return

absen_list = '\n'.join([f"{user}" for user in inactive_users.values()])
update.message.reply_text(f"Pengguna tidak aktif:\n{absen_list}")

def main(): updater = Updater("YOUR_TELEGRAM_BOT_TOKEN", use_context=True) dp = updater.dispatcher

dp.add_handler(CommandHandler("absen", absen))
dp.add_handler(CommandHandler("cek_absen", cek_absen))

updater.start_polling()
updater.idle()

if name == "main": main()

