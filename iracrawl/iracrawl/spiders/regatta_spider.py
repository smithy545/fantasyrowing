import scrapy

class RegattaSpider(scrapy.Spider):
    name = "regatta"
    allowed_domains = ["regattacentral.com"]
    start_urls = ["https://www.regattacentral.com/regattas/"]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            for table in response.xpath("//table[@id='tableResults']"):
                header = table.xpath("//thead/tr")[0]
                columns = ["Governing Body"]
                for row in header.xpath("//th/text()"):
                    columns.append(row.extract())
                for row in table.xpath("//tr"):
                    for i, element in enumerate(row.xpath("td")):
                        text = u''.join(element.xpath("node()").extract()).strip()
                        f.write(u' '.join([columns[i],":",text,"\n"]).encode('utf-8'))
