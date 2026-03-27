from .wccm import arg, three
from .wccm import output as argu
from .storage import config_load
import importlib.resources as imp
def forloop(k, msg:str="", f="config.txt"):
    print(msg)
    for i, j in k:
        print(f"{i}: {j}")

def configshow(text, name):
    text = text.strip()
    text = text.lower()
    argu = argu.strip()
    argu = argu.lower()
    cfg = config_load()
    name = name.strip()
    name = name.lower()
    with open(name or "config.txt", encoding="utf-8") as f:
        if argu == "ipa":
            for i,j in cfg["ipa"].items():
                f.write(f"{i}: {j}")
        print(f"Done! Check your IPA mappings in file '{name}'!")
    if argu == "props" or argu == "properties":
        forloop(cfg["props"].items(), "property mappings:")
    elif argu == "inv" or argu == "inventory" or argu == "inventorymapping":
        forloop(cfg["inv"].items(), "Inventory mappings:")
    elif argu == "output":
        if three == "format":
            print(f"Default format: {cfg["prefs"]["output"]["defaultFormat"]}")
        elif three == "name":
            print(f"Default name: {cfg["prefs"]["output"]["defaultFileName"]}")
        else: 
            print("Invalid third argument.")
            return
    else:
        print("Invalid second argument, please try again")
        return 

def cfgalt(mode):
    cf = config_load()
    sym, prop = three.split(" ", 1)
    match mode:
        case 0:
            cf["props"][sym] = prop 
            print(f"set {cf[sym][prop]} to {sym}") 
        case 1:
            cf[sym][prop] = sym 
            print(f"set {cf[sym][prop]} to {sym}")
# *configedit
def editcfg(conf):
    sym, prop = three.split(" ", 1)
    if argu == "props":
        conf["props"][sym][prop] = sym 
        print(f"set {conf["props"][prop]} to {sym}")
    elif argu == "inv":
        conf[argu][sym][prop] = prop
        print(f"set {conf[argu][sym][prop]} to {sym}")

    elif argu == "output":
        if sym == "format":
            conf["prefs"]["output"]["defaultFormat"] = prop 
            print(f"Set {conf["prefs"]["output"]["defaultFormat"]} to {prop}")
        elif sym == "name":
            conf["prefs"]["output"]["defaultFileName"] = prop 
            print(f"Set {conf["prefs"]["output"]["defaultFileName"]} to {prop}")
        else:
            print("Invalid argument, please try again")
            return
def search(file, keyword):
    with imp("wccm", file):
        lines = file.striplines()
        for line, i in lines:
            line = line.strip()
        print(f"Found {keyword} at index {line.find(keyword)} of line {i}")
        print(f"matches: ")

def cmd(cmd):
    match cmd:
        case "*configshow":
            configshow(arg, argu)
        case "*configedit":
            editcfg(config_load())
        case _: 
            print(f"Error: command {cmd} not recognized.")