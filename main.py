from ya_api import *
from VK_parser import *
from progress.bar import Bar


if __name__ == '__main__':
    # vk_id = int(input('Введите ID:'))
    vk_id = '10505481'
    bar = Bar('Processing', max=10)
    with open('private/token.txt', 'rt', encoding='utf-8') as f:
        ya_token = f.readline().strip('\n')
        vk_token = f.readline().strip('\n')
    ya = YandexDisk(ya_token)
    vk = Vk_pars(vk_token)
    dict = vk.get_dict_img(vk_id)
    for j in range(10):
        ya.upload_link_to_disk(dict[j]['file_name'], dict[j]['url'])
        bar.next()
    bar.finish()















