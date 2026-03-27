from .parse import parse
from .formatter import Format, markdown, inv_f
import sys 
from .storage import save, config_load, load
from .infoParse import parse_inv
from .config import set_conf
# from .cmd import cmd
from .allophones import alloparse
def main():
    
    config = config_load()
    arg = sys.argv[1]
    three = None
    if len(sys.argv) >= 3:
        output = sys.argv[2]
    elif len(sys.argv) >= 4:
        three = sys.argv[3]
   
    else:  
        output = f"{config["prefs"]["output"]["defaultFileName"]}.{config["prefs"]["output"]["defaultFormat"]}"
    #print(f"arg:{arg}")
    #print(f"output:{output}")
    text = ""

    if not arg:
        print("Usage: wccm <file> [output]")
        exit()

    elif not (arg.endswith(".wccm") or arg.endswith(".cmi") or arg.endswith(".pref") or arg.endswith(".allo")):
        print("Please use a valid file extension. Valid extensions: \n.wccm -> Lexicon \n.cmi -> inventory\n .pref -> Preferences\n.allo -> allophony")
        exit()

    cm = False
    pr = False
    al = False
    if arg.endswith(".wccm"): cm = True 
    elif arg.endswith(".pref"): pr = True
    if arg.endswith(".allo"): al = True

    if not (output.endswith(".txt") or output.endswith(".md")): 
        print("Please select a valid output extension: .md or .txt")
        print("a 'lexicon.json' file is automatically generated, if that's what you wish.")
        exit()
    if cm or pr:
        with open(arg, "r", encoding="utf-8") as f:
            text = f.read()
    if cm: 
        entries = parse(arg, text, config)
        formatted_text = ""
        if not output or output.endswith(".txt"): 
            for entry in entries:
                formatted_text += Format(entry) + "\n" + "---" + "\n"
        elif output.endswith(".md"):
            for entry in entries:
                formatted_text += markdown(entry) + "\n" + "---" + "\n"

        if not output:
            with open(f"{config["prefs"]["output"]["defaultFileName"]}.{config["prefs"]["output"]["defaultFormat"]}", "w", encoding="utf-8") as f:
                f.write(formatted_text)
        else: #output.endswith(".txt"):
            with open(output, "w", encoding="utf-8") as f:
                f.write(formatted_text)
        #elif output.endswith(".md"):
        #    with open(output, "w", encoding="utf-8") as f: 
        #       f.write(formatted_text)
        # saves data to master.json for... reasons...?? Idk man this is already here and I'm too lazy to change it
        #save(entries)

        print(f"Done! Created {output} with {len(entries)} entries.")
    elif pr: 
        save(set_conf(arg, text, config), "config.json") 

    elif al:
        save(text, "info.json")
        alloparse(text, load("info.json"))
    else: 
        inv = parse_inv(text, config)
        formatted = inv_f(inv)

        save(inv, "info.json")

        with open(output, "w", encoding="utf-8") as f:
            f.write(formatted)
        print(f"Done! created {output}.")

        