import os
from dotenv import load_dotenv
load_dotenv()          # local test के लिए

TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
DATABASE_URL         = os.environ["DATABASE_URL"]
GEMINI_API_KEY       = os.environ.get("GEMINI_API_KEY")
BLOGGER_API_KEY      = os.environ.get("BLOGGER_API_KEY")
BLOG_ID              = os.environ.get("BLOG_ID")
ADMIN_USER_ID        = int(os.environ.get("ADMIN_USER_ID", 0))
