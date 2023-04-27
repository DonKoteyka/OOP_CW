import ya_api as ya
import VK_parser as vk
import time
from progress.bar import Bar
bar = Bar('Countdown', max = 100)

if __name__ == '__main__':
    with open('token.txt', 'rt', encoding='utf-8') as f:
        ya_token = f.readline()
        vk_token = f.readline()



