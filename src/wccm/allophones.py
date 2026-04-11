from .storage import save, load, config_load
from .parse import ipa_replace
c = config_load()
ipa = c["ipa"] if not c["ipa"] is None else {}
#syntax: change i - j
def changeparse (line, conf):
    ipa = conf["ipa"]
    if not line or line.startswith("//"): pass #skips comments and empty lines 
    if not line.startswith("change"): 
        print(f"Error: missing 'change' keyword. Line:\n{line}")
        return 
    change = line.split(" ", 1)
    sound, allo = change[1].split(" - ")
    sound = sound.strip()
    allo = allo.strip()
    sound = ipa_replace(sound, ipa)
    allo = ipa_replace(allo, ipa)
    output = [sound, allo]
    return output 

#syntax: env _V
def envparse (line):
    if not line or line.startswith("//"): pass
    if not line.startswith("env"): 
        print(f"Error: missing 'env' keyword. Line:\n{line}")
        return
    env = line[4:]
    try:
        posINDEX = env.index("_")
    except ValueError:
        print("Error: position character '_' not found. \nPlease, use '_' to indicate where the sound becomes the allophone")
        return
    contextLEFT = env[:posINDEX]
    contextRIGHT = env[posINDEX+1:]
    contextRIGHT = contextRIGHT.strip()
    
    output = {
        "left": contextLEFT,
        "right": contextRIGHT,
        "raw": env
    }
    return output

def alloparse(text, info):
    rules = []
    lines = text.splitlines()
    allos = info.get("allophones", [])

    currentRULE = {}

    for line in lines:
        if line.startswith("//") or not line: pass
        elif line.startswith("change"):
            changeDATA = changeparse(line, c)
            currentRULE["input"] = changeDATA[0]
            currentRULE["output"] = changeDATA[1]
        elif line.startswith("env"):
            envDATA = envparse(line)
            currentRULE["raw"] = envDATA["raw"]
            currentRULE["env"] = {
                "left": envDATA["left"],
                "right": envDATA["right"]
            }
            if "input" in currentRULE and "output" in currentRULE:
                rules.append(currentRULE.copy())
                currentRULE = {}  
    info["allophones"] = rules 
    return info 