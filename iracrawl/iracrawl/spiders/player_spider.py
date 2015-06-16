import scrapy

from iracrawl.items import PlayerItem

class PlayerSpider(scrapy.Spider):
    name = "players"
    allowed_domains = []
    start_urls = []

    def __init__(self, *args, **kwargs):
        pass
    
    def parse(self, response):
        pass
