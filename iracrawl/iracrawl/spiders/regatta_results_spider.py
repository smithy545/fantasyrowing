import scrapy
from iracrawl.items import RegattaItem

class RegattaResults(scrapy.Spider):
    name = "results"
    allowed_domains = ["regattacentral.com"]
    start_urls = ["https://www.regattacentral.com/results",
                  "https://www.regattacentral.com/results/index.jsp?c=&year=2014&t=",
                  "https://www.regattacentral.com/results/index.jsp?c=&year=2013&t=",
                  "https://www.regattacentral.com/results/index.jsp?c=&year=2012&t=",
                  "https://www.regattacentral.com/results/index.jsp?c=&year=2011&t=",
                  "https://www.regattacentral.com/results/index.jsp?c=&year=2010&t=",
                  "https://www.regattacentral.com/results/index.jsp?c=&year=2009&t=",
                  "https://www.regattacentral.com/results/index.jsp?c=&year=2008&t=",
                  "https://www.regattacentral.com/results/index.jsp?c=&year=2007&t=",
                  "https://www.regattacentral.com/results/index.jsp?c=&year=2006&t=",
                  "https://www.regattacentral.com/results/index.jsp?c=&year=2005&t=",
                  "https://www.regattacentral.com/results/index.jsp?c=&year=2004&t=",
                  "https://www.regattacentral.com/results/index.jsp?c=&year=2003&t=",
                  "https://www.regattacentral.com/results/index.jsp?c=&year=2002&t=",
                  "https://www.regattacentral.com/results/index.jsp?c=&year=2001&t=",
                  "https://www.regattacentral.com/results/index.jsp?c=&year=2000&t=",
                  "https://www.regattacentral.com/results/index.jsp?c=&year=1999&t="]

    def parse(self, response):
        filename = response.url.split("/")[-1]
        if "year" in filename:
            filename = "regattaresults/ " + filename[18:22] + "-regattas.txt"

        with open(filename, 'wb') as f:
            for table in response.xpath("//table[@id='tableResults']"): # Table with regatta data
                columns = ["Date", "Duration", "GoverningBody", "Event", "Results", "blank", "Type", "Host", "Location", "Venue"]
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
