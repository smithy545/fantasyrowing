# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RegattaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    regatta = scrapy.Field()
    date = scrapy.Field()
    duration = scrapy.Field()
    type = scrapy.Field()
    location = scrapy.Field()
    deadline = scrapy.Field()
    late_entry = scrapy.Field()
    host = scrapy.Field()
    venue = scrapy.Field()
    url = scrapy.Field()
