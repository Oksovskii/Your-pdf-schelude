import json

jsons = """{"response": 
    {"album_id": -64, 
        "upload_url": "s",
        "user_id": 0, 
        "group_id": 178676434}}"""

pars = json.loads(jsons)
print(pars["response"]["upload_url"])