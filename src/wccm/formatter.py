from .storage import load

def Format(entry):
    text = f'{entry["word"]}'

    if "ipa" in entry:
        text += f' [{entry["ipa"]}]\n'
    else: text+="\n"
    if "meaning" in entry:
        if len(entry["meaning"]) >= 2:
            text+= "Meanings:\n"
            for m in entry["meaning"]:
                text += f'   - {m}\n'
        else:
            text+=f"Meaning: {entry["meaning"][0]}\n"

    if "plural" in entry:
        p = entry["plural"]
        if len(entry["plural"]) == 1:
            text += f'Plural: "{p[0]["word"]}" [{p[0]["ipa"]}]\n'
        elif len(entry["plural"]) == 2:
            text+=f'Plurals: {p[0]["word"]} [{p[0]["ipa"]}], {p[1]["word"]} [{p[1]["ipa"]}]\n'
        else: 
            text+='Plurals:\n'
            for i, plural in enumerate(entry["plural"]):
                text+=f'    - {plural["word"]} [{plural["ipa"]}]\n'
    
    if "gender" in entry:
        text += f'Gender: {entry["gender"]}\n'

    if "synonym" in entry: 
        text += "Synonyms: \n"
        for syn in entry["synonym"]:
            text += f"    - {syn}\n"
    
    if "antonym" in entry: 
        text += "Antonyms: \n"
        for ant in entry["antonym"]:
            text += f"    - {ant}\n"

    if "pos" in entry:
        
        if len(entry["pos"]) == 2: 
            text += f'Parts Of Speech: '
            text+=f" {entry["pos"][0]}, {entry["pos"][1]}"
        elif len(entry["pos"]) == 1:
            text += f'Part Of Speech: '
            text+=f"{entry["pos"][0]}"
        else:
            text += f'Parts Of Speech: |' 
            for pos in entry["pos"]:
                text+=f'{pos}|'    
            text += '\n'
    #text +='\n'

    if "field" in entry:
        if len(entry["field"]) == 1:
            text += f'Semantic field: {entry["field"][0]}\n'
        elif len(entry["field"]) == 2:
            text += f'Semantic fields: {entry["field"][0]}, {entry["field"][1]}\n'
        else: 
            text+='Semantic fields:  '
            for i in entry["field"]:
                text+=f'{entry["field"][i]}|'

    if "cases" in entry:
        text += 'Cases:\n'
        for case, form in entry["cases"].items():
            text += f'    - {case}: {form}\n'

    if "conjugations" in entry:
        text += 'Conjugations:\n'
        for conjugation, form in entry["conjugations"].items():
            text+=f"    - {conjugation}: {form}\n"

    if "etymology" in entry:
        text+=f"Etymology: {entry["etymology"]}\n"

    if "custom" in entry: 
        for custom, prop in entry["custom"].items():
            text+=f"{custom}: {prop}\n"
    
    if "example" in entry: 
        e = entry["example"]
        if len(entry["example"]) >= 2:
            
            text+="Example sentences: \n"
            for ex in entry["example"]: 
                text+=f"  Sentence: {ex["sentence"]}\n"
                text+=f"  Meaning: {ex["translation"]}\n"
                text+=f"  Glossing: {ex["gloss"]}\n"
                text+=f"  IPA: {ex["ipa"]}\n--\n"
        else:
            text+="Example sentence: " 
            text+=f"  {e["sentence"]}\n"
            text+=f"  Meaning: {e["translation"]}\n"
            text+=f"  Glossing: {e["gloss"]}\n"
            text+=f"  IPA: {e["ipa"]}\n"
        text+='\n'
    #print("Done! formatting complete!")
    return text

"""
=========================================
 --------------- MARKDOWN ---------------
=========================================
"""
def markdown(entry): 
    text = f'{entry["word"]}'

    if "ipa" in entry:
        text += f' *\\[{entry["ipa"]}\\]*\n'
    else: text += '\n'
    if "meaning" in entry:
        if len(entry["meaning"]) >= 2:
            text+= "**Meanings:**\n"
            for m in entry["meaning"]:
                text += f'   - *{m}*\n'
        else:
            text+=f"**Meaning:** {entry["meaning"][0]}\n"

    if "plural" in entry:
        p = entry["plural"]
        if len(entry["plural"]) == 1:
            text += f'*Plural:* "{p[0]["word"]}" [{p[0]["ipa"]}]\n'
        elif len(entry["plural"]) == 2:
            text+=f'*Plurals:* {p[0]["word"]} [{p[0]["ipa"]}], {p[1]["word"]} [{p[1]["ipa"]}]\n'
        else: 
            text+='*Plurals:*\n'
            for i, plural in enumerate(entry["plural"]):
                text+=f'    - {plural["word"]} *[{plural["ipa"]}]*\n'

    if "gender" in entry:
        text += f'**Gender:** {entry["gender"]}\n'

    if "synonym" in entry: 
        text += "**Synonyms:** \n"
        for syn in entry["synonym"]:
            text += f"    - *{syn}*\n"
    
    if "antonym" in entry: 
        text += "**Antonyms:** \n"
        for ant in entry["antonym"]:
            text += f"    - *{ant}*\n"
    
    if "pos" in entry:
        text += f'**Part Of Speech:** '
        if len(entry["pos"]) == 2: 
            text+=f" {entry["pos"][0]}, {entry["pos"][1]}"
        elif len(entry["pos"]) == 1:
            text+=f" {entry["pos"][0]}"
        else:
            for pos in entry["pos"]:
                text+=f"{pos}|"
        text+="\n"

    if "field" in entry:
        if len(entry["field"]) == 1:
            text += f'*Semantic field:* {entry["field"][0]}\n'
        elif len(entry["field"]) == 2:
            text+=f'*Semantic fields:* {entry["field"][0]}, {entry["field"][1]}.'
        else: 
            for i in entry["field"]:
                text+=f'{entry["field"][i]}|'

    if "cases" in entry:
        text += '**Cases:**\n'
        for case, form in entry["cases"].items():
            text += f'    - *{case}: {form}*\n'

    if "conjugations" in entry:
        text += '**Conjugations:**\n'
        for conjugation, form in entry["conjugations"].items():
            text+=f"    - *{conjugation}: {form}*\n"

    if "etymology" in entry:
        text+=f"Etymology: *{entry["etymology"]}*\n"

    if "custom" in entry: 
        for custom, prop in entry["custom"].items():
            text+=f"    - *{custom}: {prop}*\n"
    
    if "example" in entry: 
        e = entry["example"]
        if len(entry["example"]) >= 2:
            
            text+="*Example sentences:* \n"
            for ex in entry["example"]: 
                text+=f"    - {ex["sentence"]}\n"
                text+=f"        - Meaning: {ex["translation"]}\n"
                text+=f"        - Glossing: \n          ```{ex["gloss"]}```\n"
                text+=f"        - IPA: {ex["ipa"]}\n"
        else:
            text+="*Example sentence:* \n" 
            text+=f"    - {e["sentence"]}\n"
            text+=f"        - Meaning: {e["translation"]}\n"
            text+=f"        - Glossing:\n               ``` {e["gloss"]}```\n"
            text+=f"        - IPA: {e["ipa"]}\n"
    # print("Done! formatting complete!")
    return text

"""
===========================================================
 --------------- INVENTORY FORMATTING - TXT --------------- 
===========================================================
"""
def inv_f(dic):
    #print(f"type(dic): {type(dic)}")
    text = ""
    if len(dic["consonant"]) >0:
        text += "Consonants: \n"
        for sound in dic["consonant"]: 
            text+= f"  - {sound}\n"
    
    if len(dic["vowel"]) >0: 
        text += "Vowels: \n"
        for sound in dic["vowel"]:
            text += f"  - {sound}\n"
    
    if len(dic["tone"]) >0:
        text+= "Tones: "
        for tone in dic["tone"]:
            text +=f"{tone} "

    if len(dic["romanization"]) >0: 
        text += "Romanization:\n"
        for ipa_symbol, roman in dic["romanization"].items():
            text += f"  - {ipa_symbol} → {roman}\n"
    print("Done! formatting complete!")
    return text

"""
--------------- --------------- --------------- ----------
--------------- ALLOPHONE FORMATTING - TXT ---------------
--------------- --------------- --------------- ----------

"""
def alloTXT(data):
    text = ""
    alloz =  data.get("allophones", [])
    if not alloz: 
        return
    
    for rule in alloz: 
        env = rule.get("raw","")
        if env: 
            text += f"{rule["input"]} → {rule["output"]} / {env}\n\n"
        else: 
            text+= f"{rule["input"]} → {rule["output"]}\n\n"
    return text 

def reverse(entry):
    print("DEBUG --- reverse() called")
    text =''
    if "meaning" in entry:
        if len(entry["meaning"]) >= 2:
            text+= "Meanings:\n-"
            for m in entry["meaning"]:
                text += f'{m} - '
        else:
            text+=f"Meaning: {entry["meaning"][0]}\n"
    if "ipa" in entry:
            text += f' [{entry["ipa"]}]\n'
    else: text+="\n"

    if "plural" in entry:
        p = entry["plural"]
        if len(entry["plural"]) == 1:
            text += f'Plural: "{p[0]["word"]}" [{p[0]["ipa"]}]\n'
        elif len(entry["plural"]) == 2:
            text+=f'Plurals: {p[0]["word"]} [{p[0]["ipa"]}], {p[1]["word"]} [{p[1]["ipa"]}]\n'
        else: 
            text+='Plurals:\n'
            for i, plural in enumerate(entry["plural"]):
                text+=f'    - {plural["word"]} [{plural["ipa"]}]\n'
    
    if "gender" in entry:
        text += f'Gender: {entry["gender"]}\n'

    if "synonym" in entry: 
        text += "Synonyms: \n"
        for syn in entry["synonym"]:
            text += f"    - {syn}\n"

    if "pos" in entry:
        
        if len(entry["pos"]) == 2: 
            text += f'Parts Of Speech: '
            text+=f" {entry["pos"][0]}, {entry["pos"][1]}"
        elif len(entry["pos"]) == 1:
            text += f'Part Of Speech: '
            text+=f"{entry["pos"][0]}"
        else:
            text += f'Parts Of Speech: |' 
            for pos in entry["pos"]:
                text+=f'{pos}|'    
            text += '\n'
    #text +='\n'

    # if "field" in entry:
    #     if len(entry["field"]) == 1:
    #         text += f'Semantic field: {entry["field"][0]}\n'
    #     elif len(entry["field"]) == 2:
    #         text += f'Semantic fields: {entry["field"][0]}, {entry["field"][1]}\n'
    #     else: 
    #         text+='Semantic fields:  '
    #         for i in entry["field"]:
    #             text+=f'{entry["field"][i]}|'

    #if "cases" in entry:
    #    text += 'Cases:\n'
    #    for case, form in entry["cases"].items():
    #        text += f'    - {case}: {form}\n'

    if "conjugations" in entry:
        text += 'Conjugations:\n'
        for conjugation, form in entry["conjugations"].items():
            text+=f"    - {conjugation}: {form}\n"

    #if "etymology" in entry:
    #    text+=f"Etymology: {entry["etymology"]}\n"

    if "custom" in entry: 
        for custom, prop in entry["custom"].items():
            text+=f"{custom}: {prop}\n"
    
    if "example" in entry: 
        e = entry["example"]
        if len(entry["example"]) >= 2:
            
            text+="Example sentences: \n"
            for ex in entry["example"]: 
                text+=f"Sentence: {ex["sentence"]}\n"
                text+=f"Meaning: {ex["translation"]}\n"
                text+=f"Glossing: {ex["gloss"]}\n"
                text+=f"IPA: {ex["ipa"]}\n--\n"
        else:
            text+="Example sentence: " 
            text+=f"{e["sentence"]}\n"
            text+=f"Meaning: {e["translation"]}\n"
            text+=f"Glossing: {e["gloss"]}\n"
            text+=f"IPA: {e["ipa"]}\n"
        text+='\n'
    print(f"Done! formatting complete!\nDEBUG: text: {text}")
    return text