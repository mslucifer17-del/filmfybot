import json, re, asyncio
import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

SYSTEM = ("You are a 'Request Analyzer'. "
          "Is user asking for a movie/series? "
          'Reply ONLY JSON: {"is_request":bool,"content_title":string|null}')

async def extract_title(text: str):
    try:
        resp = await asyncio.to_thread(
            model.generate_content, f"{SYSTEM}\n\nUser: {text}"
        )
        m = re.search(r\{.*\}", resp.text, re.DOTALL)
        if m:
            d = json.loads(m.group())
            return d.get("is_request"), d.get("content_title")
    except Exception:
        pass
    return False, None
