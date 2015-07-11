#-*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LofterItem(scrapy.Item):
    # define the fields for your item here like:
    image_category = scrapy.Field()
    image_urls = scrapy.Field()
    query_url = scrapy.Field()
    description = scrapy.Field()
    
    
