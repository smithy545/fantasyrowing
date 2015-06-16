# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RegattaItem(scrapy.Item):
    GoverningBody = scrapy.Field()
    Date = scrapy.Field()
    Duration = scrapy.Field()
    Event = scrapy.Field()
    Type = scrapy.Field()
    Location = scrapy.Field()
    Deadline = scrapy.Field()
    LateEntry = scrapy.Field()
    Host = scrapy.Field()
    Venue = scrapy.Field()
    Results = scrapy.Field()
    url = scrapy.Field()
    blank = scrapy.Field()

class ClubItem(scrapy.Item):
    Blade = scrapy.Field()
    OfficialTeamName = scrapy.Field()
    ShortName = scrapy.Field()
    Abbreviation = scrapy.Field()
    Entries = scrapy.Field()
    City = scrapy.Field()
    StateRegion = scrapy.Field()
    Country = scrapy.Field()
    url = scrapy.Field()

class PlayerItem(scrapy.Item):
    name = scrapy.Field()
    height = scrapy.Field() # Centimeters
    weight = scrapy.Field() # Pounds
    year = scrapy.Field()
    sex = scrapy.Field()
    team = scrapy.Field()
