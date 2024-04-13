
from MukeshAPI import api
verse_data = api.bhagwatgita(1, 5)
print(verse_data)
@Mukesh.on_message(filters.command(["bg"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def bhagwat_Geeta(bot, message):
    
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
