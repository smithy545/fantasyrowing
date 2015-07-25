import scrapy

class RowSpider(scrapy.Spider):
    name = "row2k"
    allowed_domains = ["row2k.com"]
    start_urls = ["http://www.row2k.com/results/"]
    names = {"http://www.row2k.com/results/":2015}
    
    def __init__(self, *args, **kwargs):
        for num in range(1997,2015):
            self.start_urls.append("http://www.row2k.com/results/index.cfm?year=" + str(num))
            self.names["http://www.row2k.com/results/index.cfm?year=" + str(num)] = num
    def parse(self, response):
        filename = "row2k/" + str(self.names[response.url]) + ".html"

        tableOne = True
        with open(filename, 'wb') as f:
            for table in response.xpath("//td[@class='results-small']"):
                if not tableOne:
                    continue
                f.write(table.extract().encode("utf8"))
                tableOne = False
            f.write("test " + filename)
