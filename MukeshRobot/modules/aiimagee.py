from pyrogram import filters
from pyrogram.types import  Message
from pyrogram.types import InputMediaPhoto
from .. import pbot as  Mukesh,BOT_USERNAME
from MukeshAPI import api
from pyrogram.enums import ChatAction,ParseMode

@Mukesh.on_message(filters.command("imaginee"))
response = api.ai_image("cute boy pic")
#print(response)
with open("mukesh.jpg", 'wb') as f:
    f.write(response)
print("image generated successfully")
