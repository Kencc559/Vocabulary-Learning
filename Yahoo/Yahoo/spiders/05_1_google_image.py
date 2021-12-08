from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
from useragents import ua_list
import time
import random
import re
import os
from urllib import parse
from urllib import request
import base64


class GoogleImageSpider(object):
    def __init__(self):
        self.url = 'https://www.google.com.tw/search?q={}&tbm=isch'
        self.i = 1

    def get_image(self,url,word):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options = webdriver.Chrome()
        chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--disable-infobars')

        # browser = webdriver.Chrome(executable_path='/home/ubuntu/chromedriver',
        #                            chrome_options=chrome_options)
        browser = webdriver.Chrome(ChromeDriverManager().install(),
                                   chrome_options=chrome_options)
        # browser = webdriver.Chrome(ChromeDriverManager().install())


        # 1.
        browser.get(url)
        browser.maximize_window()

        img_link_list =[]
        start = 0
        pos = 0
        for i in range(1):
            pos += 500
            # js ='var q=document.doumentElement.scrollTop=' + str(pos)
            # js ='window.scrollTo(0,document.body.scrollHeight)'
            js ='window.scrollTo({},{})'.format(start, pos)
            browser.execute_script(js)
            start += pos
            time.sleep(2)

            img_elements = browser.find_elements_by_xpath('//div[@class="bRMDJf islir"]/img')
            # imgs = img_elements[0].get_attribute('src')
            for img_element in img_elements:
                img_link_list.append(img_element)
            print(img_elements)
            print(len(img_elements))
        print('total:',len(img_link_list))


        #
        directory = '/home/ubuntu/images/{}/'.format(word)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # 2.
        count = 0
        for img_element in img_link_list[:5]:
            count += 1
            img_link = img_element.get_attribute('src')
            # print(count,type(img_link))
            # print(img_link)
            if None is img_link:
                continue
            self.save_image(img_link, directory, word)
            time.sleep(random.randint(1, 3))
            # if count == 5:
            #     return 0

    #
    def save_image(self,img_link,directory,word):
        #
        try:
            if "http" in img_link:
                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'User-Agent': random.choice(ua_list)
                }
                html = requests.get(url=img_link,headers=headers).content
            else:
                data = img_link.split(',')
                # print(len(data), data)
                html = base64.b64decode(data[1])

            filename = directory + '{}_{}.jpg'.format(word,self.i)
            #
            with open(filename,'wb') as f:
                f.write(html)
            self.i += 1
            print('Download image {} finished!'.format(self.i-1))

        except Exception as e:
            print('Error:',e)

    #
    def run(self):
        word = input('你想要的圖片:')
        # word = "周子瑜"
        word1 = parse.quote(word)
        url = self.url.format(word1)
        print(url)
        self.get_image(url,word)

if __name__ == '__main__':
    spider = GoogleImageSpider()
    spider.run()
