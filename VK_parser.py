import requests
import json
import os.path
import pandas as pd
from pprint import pprint


def write_json(dict, ):
    if os.path.exists('photo_vk.json'):
        with open('photo_vk.json', 'w', encoding='utf-8') as f:
            json.dump(dict, f)
    else:
        with open('photo_vk.json', 'x', encoding='utf-8') as f:
            json.dump(dict, f)

def write_vk_img(url_img, file_name):
    response = requests.get(url_img)
    with open(f'{file_name}.jpg', 'wb') as f:
        f.write(response.content)

class Vk_pars:
    url = 'https://api.vk.com/method/'
    def __init__(self, token):
        self.token = token

    def get_photo_link(self, vk_id):
        url_get_photo = self.url + 'photos.getAll'
        param = {
            'owner_id' : vk_id,
            'access_token':self.token,
            # 'extended':'1',
            # 'photo_sizes':'1',
            'offset':'100',
            'v':'5.131'
        }
        res = requests.get(url_get_photo, params=param).json()

        return res['response']['items']







if __name__ == '__main__':
    with open('private/token.txt', 'rt', encoding='utf-8') as f:
        ya_token = f.readline()
        vk_token = f.readline()
        vk = Vk_pars(vk_token)
        vk_id = '52082161'
        # res = vk.get_photo_link(vk_id)
        # print(pd.DataFrame(res))
        # pprint(res)




