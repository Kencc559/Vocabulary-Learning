# -*- coding: utf-8 -*-
import base64
import os
import re
import time

import scrapy
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from ..items import YahooItem
import requests
from ..useragents import ua_list
import random

# from scrapy_redis.spiders import RedisSpider

# audio xpath: //li[@class="first"]//div[@class="compText mr-10 d-ib"]/p/span/audio/@src
# audio https://s.yimg.com/bg/dict/dreye/live/f/good.mp3

class YahooSpider(scrapy.Spider):
# class Yahoo_RedisSpider(RedisSpider):

    name = 'yahoo'
    allowed_domains = ['tw.dictionary.search.yahoo.com']
    # start_urls = ['http://tw.dictionary.search.yahoo.com/']
    one_url = 'https://tw.dictionary.search.yahoo.com/search?q={}'
    audio_url = 'https://s.yimg.com/bg/dict/dreye/live/{}/{}.mp3' # {}:m/f,{}: vocabulary
    img_url = 'https://www.google.com.tw/search?q={}&tbm=isch'
    headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'User-Agent': random.choice(ua_list)
        }
    inquireWord = input('請輸入單詞:')

    def start_requests(self):
        url = self.one_url.format(self.inquireWord)
        print(url)
        yield scrapy.Request(
            url = url,
            callback = self.get_item,
        )

    def get_item(self, response):
        # html = response.text

        item = YahooItem()
        qword = response.xpath('//div[@id="web"]//h3[@class="title lh-24"]/span/text()').get()
        if qword is None:
            print("很抱歉，字典找不到您要的資料喔！")
            return 0
        translations = response.xpath('//div[@class="compList mb-25 p-rel"]/ul/li')
        # audio_list = response.xpath('//li[@class="first"]//div[@class="compText mr-10 d-ib"]/p/span')[1]
        # print(audio_list.get())
        item['word'] = qword
        item['chinese'] = {}
        item['audio'] = self.get_audio(qword)
        item['images'] = self.get_image(qword)

        for trans in translations:
            trans_list = trans.xpath('./div/text()').getall()
            item['chinese'][trans_list[0]] = trans_list[1]
        yield item

    def get_audio(self, qword):
        """
        Get audio speech file.
        :param qword: search word
        :return: audio_file
        """
        url = self.audio_url.format('m', qword)
        html = requests.get(url=url, headers=self.headers).content
        if b'403' in html:
            url = self.audio_url.format('f', qword)
            html = requests.get(url=url, headers=self.headers).content

        if b'403' in html:
            html = None

        print(html)
        audio_file = html
        return audio_file

    def get_image(self, qword):
        """
        Get images and type of image related inquire word.
        :param qword: search word
        :return: img_dic {image1:type,image2:type_n}
        """
        url = self.img_url.format(qword)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(ChromeDriverManager().install(),
                                   chrome_options=chrome_options)
        browser.get(url)
        browser.maximize_window()
        js = 'window.scrollTo({},{})'.format(0, 1000)
        browser.execute_script(js)
        # time.sleep(1)
        img_elements = browser.find_elements_by_xpath('//div[@class="bRMDJf islir"]/img')
        # print(len(img_elements))

        imgs_dic = {}
        for element in img_elements[:5]:
            img_link = element.get_attribute('src')
            # print(img_link)
            try:
                if "http" in img_link:
                    img_type = 'jpeg'
                    img_data = requests.get(url=img_link, headers=self.headers).content
                    time.sleep(random.randint(1, 3))
                else:
                    # print(img_link)
                    base64_data = img_link.split(',')
                    string = base64_data[0]
                    pattern = '[a-z]*'
                    img_type = re.findall(pattern=pattern, string=string)[4]
                    img_data = base64.b64decode(base64_data[1])
                    # print(img_type)
                imgs_dic[img_data] = img_type

            except Exception as e:
                print('Error: ',e)
        return imgs_dic


