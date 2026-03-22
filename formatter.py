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

    return text

if __name__ == '__main__':
    entries = load()

    T = ""
    for entry in entries:
        T += Format(entry) + "\n"

    with open("lexicon.txt", "w", encoding="utf-8") as f:
        f.write(T)
