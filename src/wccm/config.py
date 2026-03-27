from .storage import save 

def set_conf(name, text, config):
    if not name.endswith(".pref"):
        print("ERROR: Please use .pref files to edit preferences.")
        return 
    lines = text.splitlines()
    #config["ipa"] = {}
    #config["inv"] = {}
    #config["prefs"]["output"] = {}
    #config["props"] = {}
    for line in lines:
        prop = ""
        val = ""
        rest = ""
        if not line.strip() or line.startswith(";"):
            continue
        if " set " not in line: 
            print(f"Error: skipping invalid line: {line}\nReason: keyword 'to' not found")
        if line.startswith(";") : continue
        
        prop, rest = line.split(" set ")
        prop = prop.strip()

        rest = rest.strip()
        if prop == "default file name":
            config["prefs"]["output"]["defaultFileName"] = rest
        elif prop == "default output format":
            config["prefs"]["output"]["defaultFormat"] = rest
        elif prop == "ipamap":
            if " to " not in rest: 
                print(f"Error: 'to' keyword missing. \nline: {line}")
                print(f"Debug: rest: {rest}, prop: {prop}")
                continue
            rest, val = rest.split(" to ")
            val = val.strip()
            if rest.strip() in config["ipa"]:
                del config["ipa"][rest.strip()]
                config["ipa"][rest.strip()] = val
            #config["ipa"][rest] = val 
        elif prop == "inventorymap":
            rest, val = rest.split(" to ")
            val = val.strip()
            if val == "vowels": val = "vowel"
            elif val == "consonants": val = "consonant"
            if rest.strip() in config["inv"]:
                del config["inv"][rest.strip()]
                config["inv"][rest.strip()] = val
            #config["inv"][rest] = val 
        elif prop == "propmap":
            if " to "not in line:
                print(f"Error: 'to' keyword missing. \nline: {line}")
            prop, rest = line.split(" set ")
            rest, val = rest.split(" to ")
            val = val.strip()
            if rest.strip() in config["props"]:
                del config["props"][rest.strip()]
                config["props"][rest.strip()] = val
            #config["props"][rest] = val 
        else:
            print(f"Error: in line {line} Keyword '{prop}' not recognized")
    save(config, "src/wccm/config.json")
    print("Done! Preferences updated successfully.")
