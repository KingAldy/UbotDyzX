import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "7555661582").split()))

API_ID = int(os.getenv("API_ID", "21165000"))

API_HASH = os.getenv("API_HASH", "1bb20345d8950cb7f07d035786a186c8")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8196311700:AAHmTtO_X3gRl40GE0mpFR3B_lEJXW95c8A")

OWNER_ID = int(os.getenv("OWNER_ID", "7555661582"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Ubot_aldyzx:ubotaldy112233@ubotdy.0tqyzbn.mongodb.net/?retryWrites=true&w=majority&appName=Ubotdy")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", ""))
