import json, re, asyncio
import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

SYSTEM = (
    "You are a 'Request Analyzer' for a Telegram bot named Manvi. "
    "Manvi's ONLY purpose is to provide MOVIES and WEB SERIES. Nothing else. "
    "Analyze the user's message below. Your task is to determine ONLY ONE THING: "
    "Is the user asking for a movie or a web series? "
    'Reply with JSON: {"is_request":bool,"content_title":string|null} '
    "Do not explain. Only JSON."
)

async def extract_title(text: str):
    try:
        resp = await asyncio.to_thread(
            model.generate_content, f"{SYSTEM}\n\nUser's Message: {text}"
        )
        m = re.search(r'\{.*\}', resp.text, re.DOTALL)   # <-- fixed quotes & raw
        if m:
            d = json.loads(m.group())
            return d.get("is_request", False), d.get("content_title")
    except Exception as e:
        pass
    return False, None
