import scrapy
from ..items import QuotetutorialItem
#from scrapy.http import Request
class QuoteSpider(scrapy.Spider):
    name='quotes'
    start_urls=[
        'https://quotes.toscrape.com/']
    def parse(self,response):
        a = QuotetutorialItem()
        all_div_quotes = response.xpath('//div[@class="quote"]')
        for quotes in all_div_quotes:
            # ipdb.set_trace()
            title = quotes.xpath(".//span[@class='text']/text()").extract()
            author = quotes.xpath(".//small[@class='author']/text()").extract()
            tags = quotes.xpath(".//a[@class='tag']/text()").extract()
            # title = quotes.css("span.text::text").extract()
            # author = quotes.css(".author::text").extract()
            # tags = quotes.css(".tag::text").extract()
            a['title'] = title
            a['author'] = author
            a['tags'] = tags
            #print(a['author'])
            # yield Request(quotes, callback=self.parse_next)
            yield a


    # def parse_next(self,response):
    #     record=QuotetutorialItem()
    #     record['title']=''.join(response.xpath("//span[@class='text']/text()").extract())
    #     record['author']=''.join(response.xpath("//small[@class='author']/text()").extract())
    #     record['tags']=''.join(response.xpath("//a[@class='tag']/text()").extract())
    #     yield record





