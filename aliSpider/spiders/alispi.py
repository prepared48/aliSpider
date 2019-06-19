# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from aliSpider.items import AlispiderItem


class AlispiSpider(CrawlSpider):
    name = 'alispi'
    allowed_domains = ['job.alibaba.com']
    start_urls = ['https://job.alibaba.com/zhaopin/positionList.html#page/0']
    pagelink = LinkExtractor(allow=("\d+"))
    rules = (
        Rule(pagelink, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # for each in response.xpath("//tr[@style='display:none']"):
        for each in response.xpath("//tr"):
            item = AlispiderItem()
            # 职位名称
            item['detail'] = each.xpath("./td[1]/span/a/@href").extract()
            # # # 详情连接
            item['workPosition'] = each.xpath("./td[3]/span/text()").extract()
            # # # 职位类别
            item['jobclass'] = each.xpath("./td[2]/span/text()").extract()
            yield item
