from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update from telegram.ext import CallbackContext

def get_main_menu(): keyboard = [ [InlineKeyboardButton("▶️ Start", callback_data="start")], [InlineKeyboardButton("ℹ️ Help", callback_data="help")], [InlineKeyboardButton("👤 Owner", callback_data="owner")], [InlineKeyboardButton("💳 Payment", callback_data="payment")], ] return InlineKeyboardMarkup(keyboard)

def start(update: Update, context: CallbackContext): update.message.reply_text("Welcome to the bot!", reply_markup=get_main_menu())

def help_command(update: Update, context: CallbackContext): update.message.reply_text("This is the help section. Use the buttons to navigate.")

def owner_info(update: Update, context: CallbackContext): update.message.reply_text("Owner: @YourUsername")

def payment_info(update: Update, context: CallbackContext): update.message.reply_text("To make a payment, visit: https://yourpaymentlink.com")

Example usage in a Telegram bot dispatcher:

from telegram.ext import Updater, CommandHandler

def main(): updater = Updater("YOUR_TELEGRAM_BOT_TOKEN", use_context=True) dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help_command))
dp.add_handler(CommandHandler("owner", owner_info))
dp.add_handler(CommandHandler("payment", payment_info))

updater.start_polling()
updater.idle()

if name == "main": main()

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update from telegram.ext import CallbackContext from .main import start  # Menghubungkan main.py ke init.py

def get_main_menu(): keyboard = [ [InlineKeyboardButton("▶️ Start", callback_data="start")], [InlineKeyboardButton("ℹ️ Help", callback_data="help")], [InlineKeyboardButton("👤 Owner", callback_data="owner")], [InlineKeyboardButton("💳 Payment", callback_data="payment")], ] return InlineKeyboardMarkup(keyboard)

def help_command(update: Update, context: CallbackContext): update.message.reply_text("This is the help section. Use the buttons to navigate.")

def owner_info(update: Update, context: CallbackContext): update.message.reply_text("Owner: @YourUsername")

def payment_info(update: Update, context: CallbackContext): update.message.reply_text("To make a payment, visit: https://yourpaymentlink.com")

all = ["start", "get_main_menu", "help_command", "owner_info", "payment_info"]

