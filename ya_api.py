import requests
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
    def upload_link_to_disk(self, file_name, link):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {
            'path':file_name,
            'url':link
        }
        response = requests.post(url = upload_url,headers = headers, params = params)
        if response.status_code == 200:
            print("Success")

if __name__ == '__main__':
    with open('private/token.txt', 'rt', encoding='utf-8') as f:
        ya_token = f.readline().strip('\n')
        vk_token = f.readline().strip('\n')
    ya = YandexDisk(ya_token)
    ya.upload_link_to_disk('VK_photo/тест', 'https://sun1.beeline-sochi.userapi.com/impg/q1HWI-b0fCBwT56X5rblwA8i-Rwko9W2FoQXYQ/FRvwFikDLQ4.jpg?size=960x1280&quality=95&sign=523121db7b994b313844595ed8ed618a&type=album')



