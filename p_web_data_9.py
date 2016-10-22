import scrapy
from urlparse import urljoin

class MyItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    submitted = scrapy.Field()

class MySpider(scrapy.Spider):
    name = "reddit"
    start_urls = [ 'https://www.reddit.com/r/learnpython/new/']
  
    
    def parse(self, response):
    
        for reddit in response.xpath('//*[@id="siteTable"]/div[@onclick="click_thing(this)"]'):
            item = MyItem()
            item['title'] = reddit.xpath('div[2]/p[1]/a/text()').extract_first() 
            item['url'] = reddit.xpath('div[2]/ul/li[1]/a/@href').extract_first()
            item['submitted']=reddit.xpath('div[2]/p[2]/a/text()').extract_first()
            print item['title']
            yield item
        
        n_page = response.xpath('//span[@class="nextprev"]//a/@href').extract_first()
        if n_page: 
            print ""
            print "--> NEXT PAGE "
            print ""
            yield scrapy.Request(n_page, callback=self.parse) 