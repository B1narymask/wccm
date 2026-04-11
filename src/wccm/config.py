from .storage import save, load
from pathlib import Path

def set_conf(name, text, config):
    configPATH = Path(__file__).parent / "config.json"
    print(f"str(configPATH): {str(configPATH)}")
    if not name.endswith(".pref"):
        print("ERROR: Please use .pref files to edit preferences.")
        return 
    lines = text.splitlines()
    default = load("default.json") #if not load("default.json") is None else {}

    print(f'type(load("default.json")): {type(load("default.json"))}')
    for i, j in default.items():
        print(f"{i}: {j}\n")
    config["ipa"] = default.get("ipa", {}).copy()
    config["inv"] = default.get("inv", {}).copy()
    config["props"] = default.get("props", {}).copy()
    config["prefs"] = default.get("prefs", {}).copy()
    for line in lines:
        prop = ""
        val = ""
        rest = ""
        if not line.strip() or line.startswith(";"):
            continue
        if " set " not in line: 
            print(f"Error: skipping invalid line: {line}\nReason: keyword 'to' not found")
            continue
        
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
            key, val = rest.split(" to ")
            val = val.strip()
            keysTOremove = [k for k, v in config["ipa"].items() if v == val]
            for k in keysTOremove:
                del config["ipa"][k]
            config["ipa"][key] = val
        elif prop == "inventorymap":
            key, val = rest.split(" to ")
            val = val.strip()
            if val == "vowels": 
                val = "vowel"
            elif val == "consonants": 
                val = "consonant"
            keysTOremove = [k for k, v in config["inv"].items() if v == val]
            for k in keysTOremove:
                del config["inv"][k]
            config["inv"][key] = val
        elif prop == "propmap":
                if " to "not in line:
                    print(f"Error: 'to' keyword missing. \nline: {line}")
                if " set " not in line: 
                    print(f"Error: 'set' keyword missing. \nline: {line}")
                    continue
                prop, rest = line.split(" set ")
                key, val = rest.split(" to ")
                val = val.strip()
                # I'm NOT putting up with this. It's 12:28 AM on a weekday, let me be.
                if val == "field" or val == "comment":
                    print("Error: due to technical difficulties, 'field' and 'comment' properties cannot be edited.")
                    print("--Sorry, Wer")
                    continue
                keysTOremove = [k for k, v in config["props"].items() if v == val]
                for k in keysTOremove:
                    del config["props"][k]
                config["props"][key] = val
        
        else:
            print(f"Error: in line {line} Keyword '{prop}' not recognized")  
    print(f"configPATH type: {type(configPATH)}")
    print(f"configPATH as string: {str(configPATH)}")
    save(config, str(configPATH))  
    print(f"FINAL config before return: {config}")
    save(config, configPATH)
    print("Done! Preferences updated successfully.")