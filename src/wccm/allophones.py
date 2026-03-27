from .storage import save, load, config_load
from .parse import ipa_replace
import sys
def alloparse(text, info):

    lines = text.splitlines()
    allos = info["allophones"]
    
    for line in lines:
        line = line.strip()
        if not line: 
            continue
        sounds, rules = line.split("/", 1)  
        phoneme, allophone = sounds.split("-", 1)
        groups, position = rules.split("_")
        info["phoneme"] = phoneme 

        phoneme = ipa_replace(phoneme, config_load())
        allophone = ipa_replace(allophone, config_load())
        phon = allos[phoneme]
        print(f"phon: {phon} \nsounds: {sounds},\nrules: {rules}, \nallos: {allos} \nallophone; {allophone}, \nphoneme:{phoneme}")
        print(f"groups: {groups}\nposition: {position}")

    
        #if rules == "_V": 
        #    phon["before"] = info["Vowel"]
        #    phon["becomes"] = allophone 
        #elif rules == "V_V":
        #    phon["before"] = info["vowel"]
        #    phon["after"] = info["vowel"]
        #    phon["becomes"] = allophone 
    #if not file.endswith(".allo"):
    #    print("please use .allo files for allophony related information.")
    #    return