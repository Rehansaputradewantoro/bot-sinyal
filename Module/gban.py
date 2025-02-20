from telegram import Update from telegram.ext import CallbackContext

Simpan daftar pengguna yang diblokir secara global

global_ban_list = set()

def gban(update: Update, context: CallbackContext): if not context.args: update.message.reply_text("Usage: /gban <user_id>") return

user_id = context.args[0]
global_ban_list.add(user_id)
update.message.reply_text(f"User {user_id} has been globally banned.")

def ungban(update: Update, context: CallbackContext): if not context.args: update.message.reply_text("Usage: /ungban <user_id>") return

user_id = context.args[0]
global_ban_list.discard(user_id)
update.message.reply_text(f"User {user_id} has been globally unbanned.")

def is_gbanned(user_id): return user_id in global_ban_list

Example integration in main.py

if name == "main": from main import main main()

