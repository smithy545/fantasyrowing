import scrapy

from iracrawl.items import ClubItem

class ClubSpider(scrapy.Spider):
    name = "clubs"
    allowed_domains = ["regattacentral.com"]
    start_urls = ["https://www.regattacentral.com/regatta/clubs/index.jsp?job_id=4122&org_id=0"]

    def parse(self, response):
        filename = "clubs.txt"
        with open(filename, 'wb') as f:
            for table in response.xpath("//table[@id='teamList']"):
                header = header = table.xpath("//thead/tr")[0]
                columns = []
                for row in header.xpath("th/text()"):
                    columns.append(''.join(e for e in row.extract() if e.isalnum()))
                for row in table.xpath("//tr"):
                    item = ClubItem()
                    temp = []                                           # List to store table data in string form before writing
                    club = ""                                           # Name of the club being parsed through
                    for i, element in enumerate(row.xpath("td")):
                        value = u''.join(element.xpath("node()").extract()).strip()
                        if i > 0:
                            item[columns[i]] = value
                            temp.append(u' '.join([columns[i],":",value,"\n"]).encode('utf-8'))
                        if i == 2: # Club long name column
                            print element
                            club = element.xpath("node()/a/text()").extract()[0].encode('utf8').strip()
                            item["url"] = element.xpath("node()/a/@href").extract()[0].encode('utf8')
                    f.write(club + "\n")
                    for line in temp:
                        f.write("\t" + line)
                    yield item
