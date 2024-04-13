
from MukeshAPI import api
verse_data = api.bhagwatgita(1, 5)
print(verse_data)
@Mukesh.on_message(filters.command(["bg"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
