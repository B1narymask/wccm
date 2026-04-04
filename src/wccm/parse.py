import sys
from .storage import config_load, save
x = sys.argv[1]
settings = config_load()
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
    symbol = sorted(props.keys(), key=len, reverse=True)
    lines = text.splitlines()
    entries = []
    current = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # try to match any symbol at the start of the line
        matched_symbol = None
        for s in symbol:
            if line.startswith(s):
                matched_symbol = s
                break

        if matched_symbol:
            value = line[len(matched_symbol):].strip()
            propNAME = props[matched_symbol]
        
        # check the first character of the line is mapped to anything
        #if symbol in props:
        #    value = line[1:].strip()
        #    prop_name = props[symbol]

            if current is None:
                current = {}

            if propNAME == "ipa":
                current["ipa_raw"] = value
                current["ipa"] = ipa_replace(value, IPA) # IPA mapping thing 

            elif propNAME == "field":
                LISTadd(current, "field", value)
            elif propNAME == "gender":
                current["gender"] = value 
            elif propNAME == "pos":
                LISTadd(current, "pos", value)
            elif propNAME == "meaning":
                LISTadd(current, "meaning", value)
            elif propNAME == "plural":
                part1 = []
                if " $ " in value: 
                    part1 = value.split(" $ ", 1)
                    dollarINDEX = value.index("$")
                    #print(part1)
                if "plural" not in current:
                    current["plural"] = []
                try:
                    current["plural"].append( {
                        "word": value[:dollarINDEX-1],
                        "ipa": ipa_replace(part1[1], IPA),
                        "identifier": f"{part1[0]}.pl"
                    })
                except IndexError:
                    print(f"Error: in line '{line}', plural parsing failed. Make sure to add a space after AND before the plural IPA (e.g., '+cats $ kAts')")
            elif propNAME == "synonym":
                LISTadd(current, "synonym", value)
            elif propNAME == "antonym":
                LISTadd(current, "antonym", value)        
            elif propNAME == "etymology":
                current["etymology"] = value
            
            # special case for grammatical cases (using ';')
            elif propNAME == "cases":
                case_, form = value.split(":", 1)
                case_ = case_.strip()
                form = form.strip()

                if not case_ or not form: 
                    raise ValueError(f"Invalid case data: {value}")

                if "cases" not in current: 
                    current["cases"] = {}
                current["cases"][case_] = form

            # special case 2, using '|' for conjugations
            elif propNAME == "conjugations": 
                conjugation, form = value.split("/", 1)
                conjugation = conjugation.strip()
                form = form.strip()

                if "conjugations" not in current: 
                    current["conjugations"] = {}
                current["conjugations"][conjugation] = form

                if not conjugation or not form:
                    raise ValueError(f"Invalid conjugation data: {value}")
            
            # special case 3: custom properties
            elif propNAME == "custom": 
                custom, val = value.split(":", 1)
                custom = custom.strip()
                val = val.strip()

                if "custom" not in current: 
                    current["custom"] = {}
                current["custom"][custom] = val
            elif propNAME == "comment": continue
            elif "pos" not in current:
                LISTadd(current, "pos", "Noun" )
            elif propNAME == "example": 
                part1 = value.split(" $ ", 1)
                sentence = part1[0].strip()
                rest = part1[1].strip()
                meaning = rest.split(" ? ", 1)
                meaning[0] = meaning[0].strip()
                meaning[1] = meaning[1].strip()
                meaning[0] = ipa_replace(meaning[0], IPA)
                gloss = meaning[1].split(" >> ")
                arrowINDEX = meaning[1].index(">>")
                if "example" not in current:
                    current["example"] = []
                current["example"].append({
                    "sentence": sentence,
                    "ipa": meaning[0], 
                    "translation": meaning[1][:arrowINDEX-1],
                    "gloss": gloss[1]
                })
            elif propNAME == "identifier": current["identifier"] = value
                
        else:
            # No property symbol found -> New word
            if current:  
                entries.append(current)
            current = {"word": line}
    
    if current: 
        entries.append(current)
    save(entries)
    
    return entries