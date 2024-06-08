from MukeshAPI import api
@Mukesh.on_message(filters.command("imaginee"))
async def imagine_(b, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
response = api.ai_image("cute boy pic")
#print(response)
with open("mukesh.jpg", 'wb') as f:
    f.write(response)
print("image generated successfully")
