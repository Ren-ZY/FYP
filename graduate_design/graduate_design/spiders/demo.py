# -*- coding: utf-8 -*-
import scrapy
from ..items import GraduateDesignItem


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['http://localhost:8080']
    start_urls = ['http://localhost:8080/product.html']

    def parse(self, response):

        items = GraduateDesignItem()
        items['image_urls'] = response.xpath('//img/@src').extract()
        yield items
