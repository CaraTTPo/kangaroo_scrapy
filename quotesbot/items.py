# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesbotItem(scrapy.Item):
    # define the fields for your item here like:
    itemName = scrapy.Field() 
    itemId = scrapy.Field() 
    skuId = scrapy.Field() 
    desc = scrapy.Field() 
    price = scrapy.Field() 
    shopId = scrapy.Field() 
    shopName = scrapy.Field() 
    showTag = scrapy.Field() 
    itemUrl = scrapy.Field() 
    updateTime = scrapy.Field() 
    deleted = scrapy.Field() 
