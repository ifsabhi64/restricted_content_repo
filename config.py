# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "20567114")
API_HASH = getenv("API_HASH", "8a5b92106e45fc6637a65a67df060a65")
BOT_TOKEN = getenv("BOT_TOKEN", "7346434214:AAHeowuE-uDWd5EdO92Qpsm2IM6BRFRQ1sA")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8036182138").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://savebot:RxxBfvkv1xnGsbPL@cluster0.9zpw7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002475194490")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
