import scrapy
from iracrawl.items import RegattaItem

class RegattaSpider(scrapy.Spider):
    name = "regattas"
    allowed_domains = ["regattacentral.com"]
    start_urls = ["https://www.regattacentral.com/regattas/"]

    def parse(self, response):
        filename = response.url.split("/")[-2] + ".txt"

        with open(filename, 'wb') as f:
            for table in response.xpath("//table[@id='tableResults']"): # Table with regatta data
                header = table.xpath("//thead/tr")[0]
                columns = ["GoverningBody"]                            # List to store column names
                for row in header.xpath("th/text()"):
                    columns.append(''.join(e for e in row.extract() if e.isalnum()))
                for row in table.xpath("//tr"):
                    item = RegattaItem()                                # Item to store information in
                    temp = []                                           # List to store table data in string form before writing
                    regatta = ""                                        # Name of the regatta being parsed through
                    for i, element in enumerate(row.xpath("td")):
                        value = u''.join(element.xpath("node()").extract()).strip()
                        item[columns[i]] = value
                        temp.append(u' '.join([columns[i],":",value,"\n"]).encode('utf-8'))
                        if i == 3: # Event column
                            regatta = element.xpath("a/text()").extract()[0].encode('utf8')
                            item["url"] = element.xpath("a/@href").extract()[0].encode('utf8')
                    f.write(regatta + "\n")
                    for line in temp:
                        f.write("\t" + line)
                    yield item
