import requests

import logging

# logging.basicConfig(
#     level=logging.DEBUG,
#     filename = "ya_api.log",
#     format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
#     datefmt='%H:%M:%S',
#     )
#
# logging.info('Hello')
class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
    def upload_link_to_disk(self, file_name, link, directory = 'VK_photo/'):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {
            'path':f'{directory}{file_name}',
            'url':link
        }
        response = requests.post(url = upload_url,headers = headers, params = params)
        if response.status_code == 202:
            print("Success")

if __name__ == '__main__':
    with open('private/token.txt', 'rt', encoding='utf-8') as f:
        ya_token = f.readline().strip('\n')
        vk_token = f.readline().strip('\n')
    ya = YandexDisk(ya_token)
    ya.upload_link_to_disk('1_2019-05-19', 'https://sun9-23.userapi.com/impf/TKJm_WUPgRCs1hW3J2n3pfUVgM8TjKckfFfVsQ/NyQS7kZm5bI.jpg?size=1500x1000&quality=96&sign=70dec2d44713d0f49e9d30b7527e86b7&c_uniq_tag=qGEbxYbNrxZN4JnZtvsCUutnD7Lgw6MCte57fzblmCU&type=album')



