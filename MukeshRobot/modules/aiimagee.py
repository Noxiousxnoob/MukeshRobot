from MukeshAPI import api
@Mukesh.on_message(filters.command("imaginee"))
async def imagine_(b, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:

        text =message.text.split(None, 1)[1]
    mukesh=await message.reply_text( "`Please wait...,\n\nGenerating prompt .. ...`")
    try:
response = api.ai_image("cute boy pic")
#print(response)
with open("mukesh.jpg", 'wb') as f:
    f.write(response)
print("image generated successfully")
