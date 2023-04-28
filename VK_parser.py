import requests
import json
import os.path
import pandas as pd
from pprint import pprint

def write_json(dict):
    if os.path.exists('photo_vk.json'):
        with open('photo_vk.json', 'w', encoding='utf-8') as f:
            json.dump(dict, f)
    else:
        with open('photo_vk.json', 'x', encoding='utf-8') as f:
            json.dump(dict, f)
class Vk_pars:
    def __init__(self, token):
        self.token = token
    def get_photo_link(self, vk_id, ):
        url = 'https://api.vk.com/method/photos.getAll'
        param = {
            'owner_id' : vk_id,
            'access_token':self.token,
            'extended':'1',
            'offset':'0',
            'v':'5.131'

        }
        res = requests.get(url, params=param)
        return res.json()


if __name__ == '__main__':
    with open('private/token.txt', 'rt', encoding='utf-8') as f:
        ya_token = f.readline()
        vk_token = f.readline()
        vk = Vk_pars(vk_token)
        vk_id = '10505481'
        res = vk.get_photo_link(vk_id)
        pprint(res)
        write_json(res)




