import json
from storage import save, config_load
import sys

x = sys.argv[1]

def ipa_replace(text, config):
    result = ""
    i = 0
    keys = sorted(config.keys(), key=len, reverse=True)
    while i < len(text):
        matched = False 
        for k in keys: 
            if text.startswith(k, i): 
                result += config[k]
                i += len(k)
                matched = True
                break 
        if not matched:
            result += text[i] 
            i += 1
    return result

def LISTadd(entry, key, val):
    if key not in entry: 
        entry[key] = []
    entry[key].append(val)


def parse(name, text, config):
    if not name.endswith(".wccm"):
        print("Error: please use a .wccm file.")
        exit()
    
    props = config["props"]
    IPA = config["ipa"]

    lines = text.splitlines()
    entries = []
    current = None

    for line in lines:
        line = line.strip()
        if not line: 
            continue

        symbol = line[0]
        
        # check the first character of the line is mapped to anything
        if symbol in props:
            value = line[1:].strip()
            prop_name = props[symbol]
            
            if current is None:
                current = {}

            if prop_name == "ipa":
                current["ipa_raw"] = value
                current["ipa"] = ipa_replace(value, IPA) # IPA mapping thing 

            elif prop_name == "field":
                current["field"] = value
            elif prop_name == "gender":
                current["gender"] = value 
            elif prop_name == "pos":
                LISTadd(current, "pos", value)
            elif prop_name == "meaning":
                LISTadd(current, "meaning", value)
            elif prop_name == "plural":
                current["plural"] = value
            elif prop_name == "synonym":
                LISTadd(current, "synonym", value)
            elif prop_name == "antonym":
                LISTadd(current, "antonym", value)        
            elif prop_name == "etymology":
                current["etymology"] = value
            
            # special case for grammatical cases (using ';')
            elif symbol == ";":
                case_, form = value.split(":", 1)
                case_ = case_.strip()
                form = form.strip()

                if not case_ or not form: 
                    raise ValueError(f"Invalid case data: {value}")

                if "cases" not in current: 
                    current["cases"] = {}
                current["cases"][case_] = form

            # special case 2, using '|' for conjugations
            elif symbol == "|": 
                conjugation, form = value.split("/", 1)
                conjugation = conjugation.strip()
                form = form.strip()

                if "conjugations" not in current: 
                    current["conjugations"] = {}
                current["conjugations"][conjugation] = form

                if not conjugation or not form:
                    raise ValueError(f"Invalid conjugation data: {value}")
            
            # special case 3: custom properties
            elif symbol == "@": 
                custom, val = value.split(":", 1)
                custom = custom.strip()
                val = val.strip()

                if "custom" not in current: 
                    current["custom"] = {}
                current["custom"][custom] = val
        else:
            # No property symbol found -> New word
            if current:  
                entries.append(current)
            current = {"word": line}
    
    if current: 
        entries.append(current)

    return entries

if __name__ == '__main__':
    entries = ""
    data = ""
    config = config_load()
    with open(x, "r") as f: 
        data = f.read()
    #config = config_load()
    entries = parse(name="main.wccm", text=data, config=config_load())
    save(entries)