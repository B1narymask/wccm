from .parse import  ipa_replace
from .storage import config_load

config = config_load() # loads configurations from config.json

# function that parses the custom inventory syntax
def parse_inv(text, config):
    props = config["inv"]
    ipa  = config["ipa"]
    #print(f"type(text): {type(text)}")
    lines = text.splitlines()
    inventory = {} 
    inventory["romanization"] = {}
    inventory["vowel"] = []
    inventory["consonant"] = []
    inventory["tone"] = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        symbol = line[0]

        if symbol in props:
            value = line[1:].strip()
            prop_name = props[symbol]
            key = prop_name 

            if key == "romanization":
                try:
                    roman, ipa_symbol = value.split(":", 1)
                    ipa_symbol = ipa_symbol.strip()
                    ipa_symbol = ipa_replace(ipa_symbol, ipa)
                    roman = roman.strip()

                    if ipa_symbol and roman: 
                        inventory["romanization"][roman] = ipa_symbol 
                except ValueError: 
                    raise ValueError(f"Invalid romanization data: {line}")
            
            elif key in ["vowel", "consonant", "tone"]:
                inventory[key].append(ipa_replace(value, ipa))
            
            else:
                if key not in inventory:
                    inventory[key] = []
                inventory[key].append(value) 
    
    print("Done! parse complete!")
    #print(f"Debug: print(inventory): \n {print(inventory)}")
    return inventory
