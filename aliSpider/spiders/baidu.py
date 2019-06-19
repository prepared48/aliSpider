# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from aliSpider.items import AlispiderItem
from scrapy.selector import Selector


class AlispiSpider(CrawlSpider):
    name = 'baidu'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['https://www.zhipin.com/c101010100-p100101/?page=2']
    pagelink = LinkExtractor(allow=("page=\d+"))
    rules = (
        Rule(pagelink, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for each in response.xpath("//div[@class='job-list']/ul"):
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            item = AlispiderItem()
        #     # 职位名称
            item['positonName'] = each.xpath("./li/div/div/h3/a/div[1]/text()").extract()[0]
        #     # # # 详情连接
            item['workPosition'] = each.xpath("./li/div/div/h3/a/span/text()").extract()[0]
        #     # # # 职位类别
            item['time'] = each.xpath("./li/div/div/h3/a/div[2]/text()").extract()[0]
            yield item
