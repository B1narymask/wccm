import json 
def save(data, file="lexicon.json"):
	with open(file or "lexicon.json", "w", encoding="utf-8") as f:
		json.dump(data, f, indent=2, ensure_ascii=False)
def load():
	with open("lexicon.json", "r", encoding="utf-8") as f:
		return json.load(f)

def config_load():
	with open("config.json", "r", encoding="utf-8") as f:
		return json.load(f)