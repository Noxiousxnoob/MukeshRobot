from MukeshAPI import api
@Mukesh.on_message(filters.command("imaginee"))
response = api.ai_image("cute boy pic")
#print(response)
with open("mukesh.jpg", 'wb') as f:
    f.write(response)
print("image generated successfully")
