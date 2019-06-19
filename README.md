a scrawler for alibaba Recruitment
安装 python

这个就不用我说了吧，网上教程一大堆

安装 scrapy 包

    pip install scrapy
    
创建 scrapy 项目

    scrapy startproject aliSpider
    
进入项目目录下，创建爬虫文件

cmd 进入项目目录，执行命令：

    scrapy genspider -t crawl alispi job.alibaba.com
    
编写 items.py 文件

    # -*- coding: utf-8 -*-
    
    # Define here the models for your scraped items
    #
    # See documentation in:
    # https://doc.scrapy.org/en/latest/topics/items.html
    
    import scrapy
    
    
    class AlispiderItem(scrapy.Item):
        # define the fields for your item here like:
        detail = scrapy.Field()
        workPosition = scrapy.Field()
        jobclass = scrapy.Field()
        
编写 alispi.py 文件

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

执行

    scrapy crawl alispi
    
输出到文件 items.json

    scrapy crawl alispi -o items.json
    
执行成功会显示如下内容



版本说明

    python 3.5.5
   

    
