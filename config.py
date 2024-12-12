from os import environ

API_ID = int(environ.get("API_ID", "28421635"))
API_HASH = environ.get("API_HASH", "a4856de5fec0b9b3601ff06425f3f58e")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002098787584"))
ADMINS = int(environ.get("ADMINS", "1534632634"))
DB_URI = environ.get("DB_URI", "mongodb+srv://PrimeRp:JNTymVXjKzBbDtiv@cluster0.rydwk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "PrimeRp")
