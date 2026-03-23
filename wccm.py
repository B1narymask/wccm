from parse import parse
from formatter import Format, markdown, inv_f
import sys 
from storage import save, config_load
from infoParse import parse_inv

config = config_load()
arg = sys.argv[1]

if len(sys.argv) >= 2:
    output = sys.argv[2]

else:  
    output = f"{config["prefs"]["output"]["defaultFileName"]}.{config["prefs"]["output"]["defaultFormat"]}"

text = ""
print(output)
if not arg:
    print("Usage: py wccm.py file.wccm output.txt or py wccm.py file.cmi output.txt")
    exit()

elif not (arg.endswith(".wccm") or arg.endswith(".cmi")):
    print("Please use a valid file extension. Valid extensions: \n.wccm\n.cmi")
    exit()

cm = False

if arg.endswith(".wccm"): cm = True 

if not (output.endswith(".txt") or output.endswith(".md")): 
    print("Please select a valid output extension: .md or .txt")
    print("a 'lexicon.json' file is automatically generated, if that's what you wish.")
    exit()

with open(arg, "r", encoding="utf-8") as f:
	text = f.read()
if cm: 
    entries = parse(arg, text, config)
    formatted_text = ""
    if not output or output.endswith(".txt"): 
        for entry in entries:
            formatted_text += Format(entry) + "\n\n" + "----" + "\n"
    elif output.endswith(".md"):
        for entry in entries:
            formatted_text += markdown(entry) + "\n\n" + "----" + "\n"

    if not output:
        with open("lexicon.txt", "w", encoding="utf-8") as f:
            f.write(formatted_text)
    elif output.endswith(".txt"):
        with open(output, "w", encoding="utf-8") as f:
            f.write(formatted_text)
    elif output.endswith(".md"):
        with open(output, "w", encoding="utf-8") as f: 
            f.write(formatted_text)
    # saves data to master.json for... reasons...?? Idk man this is already here and I'm too lazy to change it
    save(entries)

    print(f"Done! Created lexicon.txt with {len(entries)} entries.")
else: 
    inv = parse_inv(text, config)
    formatted = inv_f(inv)

    save(inv, "info.json")

    with open(output, "w", encoding="utf-8") as f:
        f.write(formatted)
