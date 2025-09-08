from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from config import TELEGRAM_BOT_TOKEN
from bot_handlers import start, handle_message, handle_callback
from database import init_db

def main():
    init_db()
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CallbackQueryHandler(handle_callback, pattern="^movie_"))
    logger.info("Bot started")
    app.run_polling(drop_pending_updates=True, close_loop=False)

if __name__ == "__main__":
    main()
