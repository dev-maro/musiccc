import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

OWNER = ["E_Z_9"]
OWNER_NAME = "𓏺 َِ𝗕َِ𝗲َِ𝗟َِ𝗮َِ𝗟 َِ𝗻َِ𝗢َِ𝘁 َِ𝗦َِ𝗵َِ𝗔َِ𝗱َِ𝗢َِ𝘄 ."
BOT_TOKEN = getenv("BOT_TOKEN")
DATABASE = getenv("MONGO_DB_URI", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
CHANNEL = "https://t.me/BE_XB"
GROUP = "https://t.me/BE_XB"
VID_SO = "https://telegra.ph/file/bf1273e084a0fb135ab5a.jpg"
PHOTO = "https://telegra.ph/file/bf1273e084a0fb135ab5a.jpg"
LOGS = "jabababbab"
