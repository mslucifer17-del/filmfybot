services:
  - type: worker
    name: filmfybot
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python main.py
    envVars:
      - key: TELEGRAM_BOT_TOKEN
        sync: false
      - key: DATABASE_URL
        sync: false
      - key: GEMINI_API_KEY
        sync: false
      - key: BLOGGER_API_KEY
        sync: false
      - key: BLOG_ID
        sync: false
      - key: ADMIN_USER_ID
        sync: false
