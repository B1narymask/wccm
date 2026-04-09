import json 
import importlib.resources 
def save(data, file="lexicon.json"):
	with open(file or "lexicon.json", "w", encoding="utf-8") as f:
		json.dump(data, f, indent=2, ensure_ascii=False)
# import traceback

"""def save(data, file="lexicon.json"):
    print(f"SAVE CALLED with data type: {type(data)}")
    if data is None:
        print("WARNING: save() received None!")
        traceback.print_stack()
    import os
    print(f"DEBUG save(): file parameter = {file}")
    print(f"DEBUG save(): resolved path = {os.path.abspath(file)}")
    with open(file or "lexicon.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"DEBUG save(): wrote to {os.path.abspath(file)}")"""
def load(file):
	with importlib.resources.open_text("wccm", file or "lexicon.json") as f:
		return json.load(f)

def config_load():
	with importlib.resources.open_text("wccm", "config.json") as f:
		return json.load(f)