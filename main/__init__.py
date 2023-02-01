#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 9728325
API_HASH = "54ac6ce26bf3c4cbe934348974b149ff"
BOT_TOKEN = "5591967334:AAGw3s52k4_SI-RAI1LmUB6PGahv5RtjZsE"
SESSION = "BQAz9mZh4jDKKiSLLzPi-iztPWEfRYWENKo0xoyQA-Da_IUVqFH_oJwl4KA6CfwveQ2BKKorxBnT4Xu9yrS_5tj3zvL6EdZld-3P47MF6mye9bDJqEmF6i_ePqiKDJ8iN-7083CaQEgpozNtWIYj4ymY-Vzagy91J1eKX-wGASFhBVfRPXzGsQWAu4fk_Qup9hjljPMSYhuHSYolDK2zpBnebCNuKz4PWLHAqCIbYEVhreSt8GYpwA1EPkesIwujeVCyZEjcnG3rkZ0MOJt3VFL1KuHiVbKk_1L8FCV5b-60sGc8rabBNyp9XyGg2DQECtFTzOhLeX2NAQRLzUPjyiVNAAAAAUD9EWgA"
FORCESUB = "tseriset"
AUTH = 5385294184

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
