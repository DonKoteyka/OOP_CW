from ya_api import *
from VK_parser import *
import time
from progress.bar import Bar
bar = Bar('Countdown', max = 100)

if __name__ == '__main__':
    with open('private/token.txt', 'rt', encoding='utf-8') as f:
        ya_token = f.readline().strip('\n')
        vk_token = f.readline().strip('\n')
    ya = YandexDisk(ya_token)
    vk = Vk_pars(vk_token)
    # vk_id = int(input('Введите ID:'))
    vk_id = '10505481'












