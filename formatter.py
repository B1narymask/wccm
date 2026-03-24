from storage import load

def Format(entry):
    text = f'{entry["word"]}'

    if "ipa" in entry:
        text += f' [{entry["ipa"]}]\n'

    if "meaning" in entry:
        if len(entry["meaning"]) >= 2:
            text+= "Meanings:\n"
            for m in entry["meaning"]:
                text += f'   - {m}\n'
        else:
            text+=f"Meaning: {entry["meaning"][0]}\n"

    if "plural" in entry:
        text += f'plural: "{entry["plural"]}"'

    text += '\n'

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
        text += f'Part(s) Of Speech:'
        if len(entry["pos"]) == 2: 
            text+=f" {entry["pos"][0]}, {entry["pos"][1]}"
        elif len(entry["pos"]) == 1:
            text+=f" {entry["pos"]}"
        else:
            for pos in entry["pos"]:
                text+=f" {pos},"

    if "field" in entry:
        text += f'Semantic field: {entry["field"]}\n'

    if "cases" in entry:
        text += 'Cases:\n'
        for case, form in entry["cases"].items():
            text += f'    - {case}: {form}\n'

    if "conjugations" in entry:
        text += 'Conjugations:\n'
        for conjugation, form in entry["conjugations"].items():
            text+=f"    - {conjugation}: {form}\n"

    if "custom" in entry: 
        for custom, prop in entry["custom"].items():
            text+=f"{custom}: {prop}"

    print("Done! formatting complete!")
    return text

def markdown(entry): 
    text = f'{entry["word"]}'

    if "ipa" in entry:
        text += f' *\\[{entry["ipa"]}]*'
    text += '\n'
    if "meaning" in entry:
        if len(entry["meaning"]) >= 2:
            text+= "**Meanings:**\n"
            for m in entry["meaning"]:
                text += f'   - *{m}*\n'
        else:
            text+=f"**Meaning:** {entry["meaning"][0]}"

    if "plural" in entry:
        text += f'plural: "{entry["plural"]}"'

    text += '\n'

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
        text += f'**Part(s) Of Speech:**'
        if len(entry["pos"]) == 2: 
            text+=f" {entry["pos"][0]}, {entry["pos"][1]}"
        elif len(entry["pos"]) == 1:
            text+=f" {entry["pos"]}"
        else:
            for pos in entry["pos"]:
                text+=f" {pos},"
        text+="\n"

    if "field" in entry:
        text += f'**Semantic field:** \\{entry["field"]}\n'

    if "cases" in entry:
        text += '**Cases:**\n'
        for case, form in entry["cases"].items():
            text += f'    - **{case}:** {form}\n'

    if "conjugations" in entry:
        text += '**Conjugations:**\n'
        for conjugation, form in entry["conjugations"].items():
            text+=f"    - **{conjugation}:** {form}\n"

    if "custom" in entry: 
        for custom, prop in entry["custom"].items():
            text+=f"-   **{custom}:** {prop}"
    # print("Done! formatting complete!")
    return text

def inv_f(dic):
    text = ""
    if "consonants" in dic:
        text += "Consonants: \n"
        for sound in dic["consonants"]: 
            text+= f"  - {sound}\n"
    
    if "vowels" in dic: 
        text += "Vowels: \n"
        for sound in dic["vowels"]:
            text += f"  - {sound}\n"
    
    if "tones" in dic:
        text+= "Tones: "
        for tone in dic["tones"]:
            text +=f"{tone} "

    if "romanization" in dic: 
        text += "Romanization:\n"
        for ipa_symbol, roman in dic["romanization"].items():
            text += f"  - {ipa_symbol} → {roman}\n"
    # print("Done! formatting complete!")
    return text

if __name__ == '__main__':
    entries = load()

    T = ""
    for entry in entries:
        T += Format(entry) + "\n"

    with open("lexicon.txt", "w", encoding="utf-8") as f:
        f.write(T)
