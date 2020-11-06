import const
import requests
import json


def get_server():
    json_data = requests.post(f'https://api.vk.com/method/photos.getMessagesUploadServer?peer_id=0&access_token={const.token}&v={const.version}')
    json_parsed = json_data.json()

    return json_parsed['response']['upload_url']

print(get_server())