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
    forms = ["txt", "md"]
    rev = False
    v = sys.argv
    config = config_load()
    In = None
    option = None
    args = v[1:]
    output = None
    for arg in args:
        if arg in ["-r", "--reverse"]:
            option = arg
            rev = True
        elif arg.startswith("-"):
            print(f"Error: Unknown optinon '{arg}'")
            return 
        elif In is None and arg.split(".")[1] in exts:
            In = arg
        elif output is None:
            #if not In is None:
            output = arg
            if output is None:
                output = f"{config["prefs"]["output"]["defaultFileName"]}.{config["prefs"]["output"]["defaultFormat"]}"
            o = output.split(".",1)

            print(f"DEBUG: o {o} | output: {output}")
            #output = arg if o[1] in forms else f"{config["prefs"]["output"]["defaultFileName"]}.{config["prefs"]["output"]["defaultFormat"]}"
            #else:
            #    print("Wer fix your shit please")
            
        # i+=1
    print(f"DEBUG: In: {In}, option: {option}, output: {output}")
    #if len(v) >= 3:
    #    output = v[2]
    #elif len(v) >= 4 and v[1].startswith("-"):
    #    option = v[1]
    #    rev = True 
    #    In = v[2]
    #elif output == "":  
    #    output = f"{config["prefs"]["output"]["defaultFileName"]}.{config["prefs"]["output"]["defaultFormat"]}"
    #print(f"In:{In}")
    #print(f"output:{output}")
    
    text = ""
    ex = In.split("."); print(f"DEBUG: ex: {ex}")
    if not In:
        print("Usage: wccm <file> <output>")
        exit()
   
    elif ex[1] not in exts:
        print("Please use a valid file extension. Valid extensions: \n.wccm -> Lexicon \n.cmi -> inventory\n .pref -> Preferences")
        print(".allo -> allophony")
        exit()

    cm = False
    pr = False
    al = False
    if In.endswith(".wccm"): cm = True 
    elif In.endswith(".pref"): pr = True
    elif In.endswith(".allo"): al = True
    out = output.split(".",1)
    # print(f"al: {al}, cm = {cm}, pr = {pr}") # -- Uncomment for debug
    if out[1] not in forms: 
        print("Please select a valid output extension: .md or .txt")
        print("a 'lexicon.json' file is automatically generated, if that's what you wish.")
        exit()
    #if cm or pr:
    with open(In, "r", encoding="utf-8") as f:
        text = f.read()
    print(rev)
    if cm: 
        entries = parse(In, text, config)
        formatted_text = ""
        if not output or output.endswith(".txt"): 
            for entry in entries:
                formatted_text += Format(entry) + "\n" + "---" + "\n"
        elif output.endswith(".md"):
            for entry in entries:
                formatted_text += markdown(entry) + "\n" + "---" + "\n"


            with open(output, "w", encoding="utf-8") as f:
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
        set_conf(In, text, config)
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
    elif rev:
        entries = parse(In, text, config)
        print(f"entries {entries}")
        print(type(entries))
        formatted = ""
        for entry in entries:
            formatted += reverse(entry) + "\n" + "---" + "\n"
        with open(output, "w", encoding="utf-8") as f:
            f.write(formatted)
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