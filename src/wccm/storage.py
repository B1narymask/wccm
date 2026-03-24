import json 
import importlib.resources 
def save(data, file="lexicon.json"):
	with importlib.resources.open_text("wccm", file or "lexicon.json") as f:
		json.dump(data, f, indent=2, ensure_ascii=False)
def load():
	with importlib.resources.open_text("wccm", "lexicon.json") as f:
		return json.load(f)

def config_load():
	with importlib.resources.open_text("wccm", "config.json") as f:
		return json.load(f)