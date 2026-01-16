from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)
import re
import os

TOKEN = os.getenv("8042508913:AAE6CwJ7lJIKe4tpkb-RR652Qq9Yga7SucQ")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! 👋\n"
        "Напиши: проблема на 6233\n"
        "Команда /help — помощь"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Формат:\n"
        "проблема на номер\n\n"
        "Пример:\n"
        "замена масла на 6233"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    match = re.search(r"(.*)\s+на\s+(\d+)", text)
    if not match:
        await update.message.reply_text("Неверный формат")
        return

    problem = match.group(1).strip()
    bus_number = match.group(2)

    await update.message.reply_text(
        f"Автобус: {bus_number}\n"
        f"Проблема: {problem}"
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
