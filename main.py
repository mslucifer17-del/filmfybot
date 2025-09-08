import logging, asyncio
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TELEGRAM_BOT_TOKEN
from database import init_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update, _):
    await update.message.reply_text("🎬 Send me any movie name!")

async def echo(update, _):
    await update.message.reply_text("I am alive!")

def main():
    init_db()
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    logger.info("Bot started")
    app.run_polling(drop_pending_updates=True, close_loop=False)

if __name__ == "__main__":
    main()
