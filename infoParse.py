from parse import  ipa_replace
from storage import config_load
import sys 

file = sys.argv[1]
config = config_load() # loads configurations from config.json

# function that parses the custom inventory syntax
def parse_inv(text, config):
    props = config["inv"]
    ipa  = config["ipa"]

    lines = text.splitlines()
    inventory = {}  
    inventory["romanization"] = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue
        symbol = line[0]

        if symbol in props:
            value = line[1:].strip()
            prop_name = props[symbol]

            key = prop_name 

            if key not in inventory:
                inventory[key] = []

            inventory[key].append(ipa_replace(value, ipa))

        elif symbol == "¡":
            continue  # skip comments
        
        elif symbol == "-":
            value = line[1:].strip()
            try:
                roman, ipa_symbol = value.split(":", 1)
                ipa_symbol = ipa_symbol.strip()
                ipa_symbol = ipa_replace(ipa_symbol, ipa)
                roman = roman.strip()
                
                if ipa_symbol and roman: 
                    inventory["romanization"][roman] = ipa_symbol 

            except ValueError: 
                raise ValueError(f"Invalid romanization data: {line}")

    #save(inventory, "info.json") # saves entries for... why do I save? Oh whatever it's already there.
    print("Done! parse complete!")
    return inventory
    
"""
text = ""
with open(file, "r") as f:
    text = f.read()
parse_inv(text,config)
"""