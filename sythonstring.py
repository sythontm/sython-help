from telethon.sync import TelegramClient
from telethon.sessions import StringSession

APP_ID = int(input("1 - APP ID : "))
API_HASH = input("2 - API HASH : ")

with TelegramClient(    StringSession(),     APP_ID, 
    API_HASH
) as client:
    session_str = client.session.save()
    s_m = client.send_message("me", session_str)
    s_m.reply("TERMUX CODE BY SOURCE SYTHON | لاتشارك الكود مع أحد لان من الممكن اختراق الحساب")
    print("✅ check your Telegram Saved Messages ✅"
