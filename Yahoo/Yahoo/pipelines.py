# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os
import time

import redis


class YahooPipeline(object):
    def __init__(self):
        self.redis_db = redis.Redis(host='127.0.0.1',port=6379, db=0)

    def process_item(self, item, spider):
        print(item)
        self.redis_db.flushdb()
        qword = item['word']
        chinese_json = json.dumps(item['chinese'])
        if item['audio'] != None:
            audio_path = self.save_audio(qword, item['audio'])
        else:
            audio_path = 'No Audio File.'
        images_path = self.save_images(qword, item['images'])
        self.redis_db.hset(qword, 'chinese', chinese_json)
        self.redis_db.hset(qword, 'audio', audio_path)
        self.redis_db.hset(qword,'images',images_path)

        print(qword)
        self.printOut(qword, 'chinese')
        print(self.redis_db.hget(qword, 'audio').decode())
        self.printOut(qword, 'images')
        return item

    def printOut(self, qword, pout):
        out_json = self.redis_db.hget(qword, pout)
        out_dic = json.loads(out_json)
        for k, v in out_dic.items():
            print(k, v)

    def save_audio(self, word, audio):
        """
        save audio file.
        :param word: inquire word
        :param audio: audio file
        :return: file
        """
        directory = '/home/ubuntu/TeduProject/audio/'
        if not os.path.exists(directory):
            os.makedirs(directory)
        file = directory + '{}.mp3'.format(word)
        with open(file, 'wb') as f:
            f.write(audio)
        return file

    def save_images(self, word, images):
        """
        save image files.
        :param word: inquire word
        :param images: image files {image:extend_file_name}
        :return: json.dumps(file_dic)
        """
        # images = {image_data : image_type}
        num = 0
        directory = '/home/ubuntu/TeduProject/images/{}/'.format(word)
        if not os.path.exists(directory):
            os.makedirs(directory)

        file_dic = {}
        for image,itype in images.items():
            num += 1
            fname = '{}_{}.{}'.format(word,num,itype)
            file = directory + fname
            file_dic[fname] = file
            with open(file, 'wb') as f:
                f.write(image)
        return json.dumps(file_dic)

