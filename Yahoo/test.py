import requests
from useragents import ua_list
import random



url = "https://s.yimg.com/bg/dict/dreye/live/f/family.mp3"
headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'User-Agent': random.choice(ua_list)
        }
html = requests.get(url=url,headers=headers)
print(html)

# with open('/home/ubuntu/TeduProject/audio/1.mp3', 'wb') as f:
#     f.write(html)

if __name__ == '__main__':
    pass