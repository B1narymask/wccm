from parse import parse
from formatter import Format
import sys 
from storage import save, config_load

arg = sys.argv[1]
config = config_load()
text = ""
with open(arg, "r", encoding="utf-8") as f:
	text = f.read()
entries = parse(arg, text, config)

formatted_text = ""
for entry in entries:
    formatted_text += Format(entry) + "\n\n" + "-"*40 + "\n\n"

# write the formatted text to the lexicon file
with open("lexicon.txt", "w", encoding="utf-8") as f:
    f.write(formatted_text)

# saves data to master.json for... reasons...?? Idk man this is already here and I'm too lazy to change it
save(entries)

print(f"Done! Created lexicon.txt with {len(entries)} entries.")