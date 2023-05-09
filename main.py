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
    # vk_id = '10505481'
    with open('private/token.txt', 'rt', encoding='utf-8') as f:
        ya_token = f.readline().strip('\n')
        vk_token = f.readline().strip('\n')
    ya = YandexDisk(ya_token)
    vk = Vk_Avatar(vk_token)
    dict = vk.get_dict_img(vk_id, 10)
    bar = Bar('Processing', max=len(dict))
    for j in dict:
        ya.upload_link_to_disk(str(j['file_name']), str(j['url']))
        bar.next()
    bar.finish()














