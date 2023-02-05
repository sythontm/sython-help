from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID")
APP_HASH = os.environ.get("APP_HASH")
BOT_USERNAME = os.environ.get("BOT_USERNAME")
session = os.environ.get("TERMUX")
SESSION = os.environ.get("TERMUX")
sython = TelegramClient(StringSession(session), APP_ID, APP_HASH)
ispay = ['yes']
ispay2 = ['yes']

