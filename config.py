import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6379092218:AAEpK-LrnSMGCejlxzvw5AS9NHExgRlpF-o")
API_ID = int(os.environ.get("API_ID", "26670684"))
API_HASH = os.environ.get("API_HASH", "60592bded0f25a9633a8133601f2c779")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "1984672629"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
