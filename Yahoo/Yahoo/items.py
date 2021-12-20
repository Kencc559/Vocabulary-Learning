# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YahooItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    word = scrapy.Field()
    chinese = scrapy.Field()
    audio = scrapy.Field()
    images = scrapy.Field()

