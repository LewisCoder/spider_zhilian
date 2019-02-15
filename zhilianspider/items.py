# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhilianspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field()
    job_link = scrapy.Field()
    job_info = scrapy.Field()
    job_tags = scrapy.Field()

    company = scrapy.Field()
    address = scrapy.Field()
    salary = scrapy.Field()
    pass