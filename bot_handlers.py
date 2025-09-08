from telegram import Update
from telegram.ext import ContextTypes
from ai_utils import extract_title
from fuzzy_search import smart_search
from keyboards import movie_buttons, choose_movie

async def start(update: Update, _: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎬 Send me any movie/series name!")

async def handle_message(update: Update, _: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    is_req, title = await extract_title(text)
    if not is_req:
        return
    movies = await smart_search(title or text)
    if not movies:
        await update.message.reply_text("😔 Not found – I'll notify when added!")
    elif len(movies) == 1:
        t, u = movies[0]
        await update.message.reply_text(f"🍿 *{t}*", parse_mode="Markdown", reply_markup=movie_buttons(t, u))
    else:
        await update.message.reply_text("🔍 Choose one:", reply_markup=choose_movie(movies))

async def handle_callback(update: Update, _: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    url = query.data.replace("movie_", "")
    await query.message.reply_text("🎬 Here you go!", reply_markup=movie_buttons("Selected Movie", url))
