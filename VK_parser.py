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
        swicher = True
        while swicher:
            param = {
                'owner_id' : vk_id,
                'access_token':self.token,
                'offset':offset,
                'v':'5.131'
            }
            res = requests.get(url_get_photo, params=param).json()
            if len(res['response']['items']) < 20:
                swicher = False
            res_total += res['response']['items']
            offset += 20
            time.sleep(0.33)
        return res_total
    def get_dict_img(self, vk_id):
        vk_dic = self.get_photo_link(vk_id)
        j_list = list()
        size_dict = {'s': 1, 'm': 2, 'o': 3, 'p': 4, 'q': 5, 'r': 6, 'x': 7, 'y': 8, 'z': 9, 'w': 10}
        for i in vk_dic:
            file_url = max(i['sizes'], key=lambda x: size_dict[x["type"]])
            j_dic = {
                "file_name": i['id'],
                "url": file_url['url'],
                "type": file_url['type']
            }
            j_list.append(j_dic)
        return j_list

    def write_img_json(self, vk_id,  json_name = 'photo_vk.json'):
        dict_img = self.get_dict_img(vk_id)
        [x.pop('url') for x in dict_img]
        if os.path.exists(f'{json_name}'):
            with open(f'{json_name}', 'w', encoding='utf-8') as f:
                json.dump(dict_img, f)
        else:
            with open(f'{json_name}', 'x', encoding='utf-8') as f:
                json.dump(dict_img, f)


    def write_photo_img(self, vk_id, dir = 'photo'):
        dict_img = self.get_dict_img(vk_id)
        if os.path.exists(f'{dir}/'):
            for i in dict_img:
                response = requests.get(i['url'])
                with open(f'{dir}/{i["file_name"]}.jpg', 'wb') as f:
                    f.write(response.content)
        else:
            return 'Укажите имя папки для сохранения фото'




if __name__ == '__main__':
    with open('private/token.txt', 'rt', encoding='utf-8') as f:
        ya_token = f.readline()
        vk_token = f.readline()
    vk = Vk_pars(vk_token)
    vk_id = '10505481'
    # # res = vk.get_dict_img(vk_id)
    res = vk.get_photo_link(vk_id)
    # res = vk.write_img_json(vk_id)
    # res = vk.write_photo_img(vk_id)
    # vk.get_photo_img(vk_id)
    # print(pd.DataFrame(res))
    pprint(res)
    # print(len(res))





