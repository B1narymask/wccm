from .parse import parse
from .formatter import Format, markdown, inv_f, alloTXT, reverse
import sys 
from .storage import save, config_load, load
from .infoParse import parse_inv
from .config import set_conf
from .allophones import alloparse
from pathlib import Path
infoPATH = Path(__file__).parent / "info.json"
configPATH = Path(__file__).parent / "config.json"
alloPATH = Path(__file__).parent / "allophony.json"
def main():
    exts = ["wccm", "cmi", "pref", "allo"]
    config = config_load()
    arg = sys.argv[1]
    rev = None
    revBOOL = False
    if len(sys.argv) >= 3:
        output = sys.argv[2]
    else:  
        output = f"{config["prefs"]["output"]["defaultFileName"]}.{config["prefs"]["output"]["defaultFormat"]}"
    #print(f"arg:{arg}")
    #print(f"output:{output}")
    if len(sys.argv) >= 4:
        rev = sys.argv[3]
        rev = rev.lower()
        revBOOL = True
        if rev not in ["reverse", "eng"]: 
            print(f"Error: option '{rev}' not recognized.")
            revBOOL = False
            return

    text = ""
    ex = arg.split(".")
    if not arg:
        print("Usage: wccm <file> [output] [mode]")
        exit()

    elif ex[1] not in exts:
        print("Please use a valid file extension. Valid extensions: \n.wccm -> Lexicon \n.cmi -> inventory\n .pref -> Preferences")
        print(".allo -> allophony")
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
    #if cm or pr:
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
        set_conf(arg, text, config) 
    elif al:
        #save(alloparse())
        save(alloparse(text, load("allophony.json")), alloPATH)
        save(alloparse(text, load("allophony.json")), "allophony.json")
        form = alloTXT(alloparse(text, config))
        if output.endswith(".txt"):
            with open(output, "w", encoding="utf-8") as f: 
                f.write(form)
            print(f"Done! created '{output}'")
        else: 
            print("Heeeeyyyy... allo files (and cmi files) only support .txt output as of this version, \n-sorry, Wer (;'v)")
    
    else: 
        inv = parse_inv(text, config)
        formatted = inv_f(inv)
        #print(f"inv: {inv}\nformatted: \n{formatted}")
        save(inv, infoPATH)
        if output.endswith(".txt"):
            with open(output, "w", encoding="utf-8") as f:
                f.write(formatted)
            print(f"Done! created '{output}'.")
        else: 
            print("Heeeeyyyy... cmi files (and allo files) only support .txt output as of this version, \n-sorry, Wer (;'v)")
    if revBOOL:
        entriez = parse(arg, text, config)
        formattedTEXT = ""
        for entry in entriez:
            formattedTEXT += reverse(entry) + "\n" + "---" + "\n"
        with open(output, "w", encoding="utf-8") as f:
            f.write(formattedTEXT)