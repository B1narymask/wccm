from .storage import save 

def set_conf(name, text, config):
    if not name.endswith(""):
        print("ERROR: Please use .pref files to edit preferences.")
        return 
    lines = text.splitlines()
    for line in lines:
        sym = line[0]
       
        if sym == ":":
            key, val = line.split(".", 1)
            print(f"key: {key[1:]}, val: {val}")
            config["ipa"][key[1:]] = val 
        elif sym == ",":
            key, val = line.split(".", 1)
            config["props"][key[1:]] = val 
            print(f"key: {key[1:]}, val: {val}")
        elif sym == "/":
            key, val = line.split(".", 1)
            print(f"key: {key[1:]}, val: {val}")
            config["inv"][key[1:]] = val
        elif sym=="?":
            key, val = line.split(".", 1)
            print(f"key: {key[1:]}, val: {val}")
            config["prefs"]["output"][key[1:]] = val
        elif sym == ";": continue # ignore comments
        
    save(config, "config.json")
    print("Done! Preferences updated successfully.")