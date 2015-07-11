# -*- coding: utf-8 -*-

from scrapy.selector import Selector
import scrapy
from scrapy.contrib.loader import ItemLoader, Identity
from lofter.items import LofterItem
import os

class LofterSpider(scrapy.Spider):
    name = "lofter"
    allowed_domains = ["joystore.lofter.com"]
    start_urls = (
          'http://joystore.lofter.com',
    )

    def parse(self, response):
        sel = Selector(response)
        for link in sel.xpath('//div[@class="m-post m-post-img   "]/div[@class="ct"]/div[@class="ctc box"]/div[@class="pic"]/a/@href').extract():
            request = scrapy.Request(link, callback=self.parse_item)
            yield request

        pages = sel.xpath('//div[@id="m-pager-idx"]/a/@href').extract()
        if len(pages) > 1:
           page_link = pages[-1]
           request = scrapy.Request('http://joystore.lofter.com/%s' %page_link, callback=self.parse)
           yield request
    
    def parse_item(self, response):
        l = ItemLoader(item=LofterItem(), response=response)
        l.add_xpath('image_urls', '//div[@class="pic"]/a/img/@src', Identity())
        l.add_xpath('image_category', '//div[@class="tags box"]/a/text()')
        l.add_xpath('description','//div[@class="text"]/p/text()')
     
        l.add_value('query_url', response.url)
        return l.load_item() 
