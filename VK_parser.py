import requests
import json
import os.path
import time
# import pandas as pd
from pprint import pprint

class Vk_pars:
    url = 'https://api.vk.com/method/'
    def __init__(self, token):
        self.token = token

    def get_photo_link(self, vk_id):
        url_get_photo = self.url + 'photos.getAll'
        res_total = list()
        offset = int()
        while True:
            if offset == 3000:
                break
            param = {
                'owner_id' : vk_id,
                'access_token':self.token,
                # 'extended':'1',
                # 'photo_sizes':'1',
                'offset':offset,
                'v':'5.131'
            }
            res = requests.get(url_get_photo, params=param).json()['response']['items']
            res_total += res
            offset += 20
            time.sleep(0.33)
        return res_total
    def get_json_img(self, vk_id):
        vk_dic = self.get_photo_link(vk_id)
        j_list, val_1, val_2, link = list(), str(), int(), list()
        for i in vk_dic:
            for index, size_dict in enumerate(i['sizes']):
                if size_dict['type'] > val_1:
                    val_1 = size_dict['type']
                    val_2 = index
            link.append(i['sizes'][val_2]['url'])
            j_dic = {
                "file_name": i['id'],
                "size": i['sizes'][val_2]['type']
            }
            j_list.append(j_dic)
        return j_list, link
    def write_json_img(self, vk_id, json_name = 'photo_vk.json'):
        j_list = self.get_json_img(vk_id)[0]

        if os.path.exists(f'{json_name}'):
            with open(f'{json_name}', 'w', encoding='utf-8') as f:
                json.dump(j_list, f)
        else:
            with open(f'{json_name}', 'x', encoding='utf-8') as f:
                json.dump(j_list, f)

    def get_photo_img(self, vk_id, dir = 'photo'):
        list_links = self.get_json_img(vk_id)[0]
        list_names = self.get_json_img(vk_id)[1]
        for link, file_name in zip(list_links, list_names):
            response = requests.get(link)
            with open(f'{dir}/{file_name}.jpg', 'wb') as f:
                f.write(response.content)


if __name__ == '__main__':
    with open('private/token.txt', 'rt', encoding='utf-8') as f:
        ya_token = f.readline()
        vk_token = f.readline()
    vk = Vk_pars(vk_token)
    vk_id = '52082161'
    # res = vk.write_json_img(vk_id)
    res = vk.get_photo_link(vk_id)
    # res = vk.get_json_img(vk_id)
    # vk.get_photo_img(vk_id)
    # print(pd.DataFrame(res))
    pprint(res)
    print(len(res))





