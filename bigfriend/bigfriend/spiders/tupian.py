# -*- coding: utf-8 -*-
import scrapy


class TupianSpider(scrapy.Spider):
    name = 'tupian'
    allowed_domains = ['tupian.com']
    start_urls = ['http://tupian.com/']

    def parse(self, response):
        pass
