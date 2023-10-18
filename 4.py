import datetime
import time
import pyrogram
from pyrogram import Client
import requests
import os
from time import sleep
from pyrogram.errors import FloodWait, BadRequest
tok = "5906668751:AAEaqJCi5zVqALWuuoMMYszYhl2OCA2c1Es"
idown = 5345637082
qq = 0
session = "BAGMcpgAZ927Mha1e7TUiXv3tLskqGDAXTjR5TyCVUVShyK4dllKmaBRuApqdQHEZoU7rZ4ryUaEFIvm7PpfjdMS1d3INzwP_V7zNCU5q0GrHDh8iNXXLsaotC_gPJ-7c-5yEGDg1qvDFhnWlMenbllfsyKt0Hph29XzDDElWgGG9cHYgh7iRGprNG9P5GbQv9dXhTAU2uu3HqOEnb4CKBEZ3QzCLibnXPGCP9rJ8PfLod6sXqncSTuY0BTe5HMGzCgV3ufxZDvIye09N0pcQVjpzLY7h4Efhq6YJPCDoBZ0gZIWP7fA4NhSZaQFIqWaFA0KaHezODzqM6wDkUPLFd-xS5jrvgAAAABM9-r9AA"
app = Client("ACCC", api_id=26022994, api_hash="2e84a6b68bd6b5a79f46e8192668e0ea", session_string=session)
ok = requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=𝐆𝐨 𝐅𝐨𝐫 𝐅𝐮𝐜𝐤𝐢𝐧𝐠 !')
username = open("user.txt").read().split("\n")
app.start()
while True:
    qq += 1
    for user in username:
        if user != "":
            print(qq)
            try:
                peer = app.resolve_peer(user)
                app.invoke(pyrogram.raw.functions.messages.get_peer_dialogs.GetPeerDialogs(peers=[peer]))
            except:
                app.set_username(user)  
