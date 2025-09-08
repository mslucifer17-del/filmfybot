from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def movie_buttons(title: str, url: str) -> InlineKeyboardMarkup:
    kb = [[InlineKeyboardButton("📥 Download", url=url)]]
    return InlineKeyboardMarkup(kb)

def choose_movie(movies: list[tuple[str, str]]) -> InlineKeyboardMarkup:
    kb = [[InlineKeyboardButton(t, callback_data=f"movie_{u}")] for t, u in movies]
    return InlineKeyboardMarkup(kb)
