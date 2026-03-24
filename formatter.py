from storage import load

def Format(entry):
    text = f'{entry["word"]}'

    if "ipa" in entry:
        text += f' [{entry["ipa"]}]'

    if "meaning" in entry:
        text += f': "{entry["meaning"]}"'

    if "plural" in entry:
        text += f', plural: "{entry["plural"]}"'

    text += '\n'

    if "gender" in entry:
        text += f'Gender: {entry["gender"]}\n'

    if "synonym" in entry: 
        text += "Synonyms:"
        for syn in entry["synonym"].items():
            text += f"\n  - {syn}"
    
    if "antonym" in entry: 
        text += "Antonyms:"
        for ant in entry["antonym"].items():
            text += f"\n  - {ant}"

    if "pos" in entry:
        text += f'P.O.S: {entry["pos"]}\n'

    if "field" in entry:
        text += f'Semantic field: {entry["field"]}\n'

    if "cases" in entry:
        text += 'Cases:\n'
        for case, form in entry["cases"].items():
            text += f'  {case}: {form}\n'

    if "conjugations" in entry:
        text += 'Conjugations:\n'
        for conjugation, form in entry["conjugations"].items():
            text+=f"  {conjugation}: {form}\n"

    if "custom" in entry: 
        for custom, prop in entry["custom"].items():
            text+=f"{custom}: {prop}"

    print("Done! formatting complete!")
    return text

def markdown(entry): 
    text = f'{entry["word"]}'

    if "ipa" in entry:
        text += f'*\\[{entry["ipa"]}]*'

    if "meaning" in entry:
        text += f': "{entry["meaning"]}"'

    if "plural" in entry:
        text += f', plural: "{entry["plural"]}"'

    text += '\n'

    if "gender" in entry:
        text += f'**Gender:** {entry["gender"]}\n'

    if "synonyms" in entry: 
        text += "***Synonyms:***"
        for syn in entry["synonyms"].items():
            text += f"\n  - *{syn}*"
    
    if "antonyms" in entry: 
        text += "***Antonyms:***"
        for ant in entry["antonyms"].items():
            text += f"\n  - *{ant}*"
    
    if "pos" in entry:
        text += f'**Part Of Speech:** {entry["pos"]}\n'

    if "field" in entry:
        text += f'**Semantic field:** {entry["field"]}\n'

    if "cases" in entry:
        text += '**Cases:**\n'
        for case, form in entry["cases"].items():
            text += f'  - **{case}:** {form}\n'

    if "conjugations" in entry:
        text += '**Conjugations:**\n'
        for conjugation, form in entry["conjugations"].items():
            text+=f"  - **{conjugation}:** {form}\n"

    if "custom" in entry: 
        for custom, prop in entry["custom"].items():
            text+=f"- **{custom}:** {prop}"
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
