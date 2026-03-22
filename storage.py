import json 
def save(data):
	with open("master.json", "w", encoding="utf-8") as f:
		json.dump(data, f, indent=2, ensure_ascii=False)
def load():
	with open("master.json", "r", encoding="utf-8") as f:
		return json.load(f)

def config_load():
	with open("config.json", "r", encoding="utf-8") as f:
		return json.load(f)