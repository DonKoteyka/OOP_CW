from ya_api import *
from VK_parser import *
from progress.bar import Bar
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename = f"{__name__}.log",
    format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    )

logging.info('Hello')


if __name__ == '__main__':
    vk_id = int(input('Введите ID:'))
    # ya_token = input('Введите токен от яндекс диска:')
    # vk_id = '1'
    # with open('private/token.txt', 'rt', encoding='utf-8') as f:
    #     ya_token = f.readline().strip('\n')
    #     vk_token = f.readline().strip('\n')
    ya = YandexDisk(ya_token)
    vk = Vk_Avatar(vk_token)
    dict = vk.get_dict_img(vk_id, 5)
    # vk.write_img_json(vk_id)
    bar = Bar('Processing', max=len(dict))
    for j in dict:
        ya.upload_link_to_disk(j['file_name'], j['url'])
        bar.next()
    bar.finish()














