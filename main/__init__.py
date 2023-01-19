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
SESSION = "BQBhZBClkvxuVweCn6HyQAOyY0_tubTQGOxOfGeF_VK_dN2WkJW2r9AjwvPWG4qYucDsmnteNmA4vk9AP8UW5NTVQyK9_bIQhvTaB5fEk08CoPMWvLSrBEvttcIph5y7VczPBhWRvlKNMQk0bly6LLTjFfjXNyVGitcn6---08Qtm2qQLH2XDitHLrYSZjelEZscMzUTOiEaUoYq212uZhnY2ybCV6GmNNgctp5OKc0RM88CcBufjVHpdNNtIqfi9Z1LHVgnDcnxF1pR77usknuF4qhC3VvMJa04hkE1m01m04_G4DYGFY0ctM2huKh84PXgkh73KAaiRxL_c5UfycKOAAAAAUD9EWgA"
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
