import json

from settings import _MAKESJSON

# load makes and models from json file
def load_makes(website: str) -> dict:
    with open(_MAKESJSON, "r", encoding="utf-8", newline="") as mjson:
        data = mjson.read()
        makes_dict = json.loads(data)
    return makes_dict[website]
