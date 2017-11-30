# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanBookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    price=scrapy.Field()
    edition_year=scrapy.Field()
    publisher=scrapy.Field()
    ratings=scrapy.Field()
    author=scrapy.Field()

class DoubanMailItem(scrapy.Item):
    sender_tiem=scrapy.Field()
    sender_from=scrapy.Field()
    url=scrapy.Field()
    title=scrapy.Field()

class DoubanMailItem(scrapy.Item):
    sender_time = scrapy.Field()     # 发送时间
    sender_from = scrapy.Field()     # 发送人
    url = scrapy.Field()             # 豆邮详细地址
    title = scrapy.Field()           # 豆邮标题

