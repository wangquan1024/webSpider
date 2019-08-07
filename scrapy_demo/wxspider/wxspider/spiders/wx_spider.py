# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wxspider.items import WxspiderItem

# CrawlSpider是爬取那些具有一定规则网站的常用的爬虫，它基于Spider并有一些独特属性
class WxSpiderSpider(CrawlSpider):
    name = 'wx_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    #  follow是否跟进,设置为true会确认一直跟进爬取具有相同规则的页面
    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d+'),follow=True),
        Rule(LinkExtractor(allow=r'.+article.+\.html'),callback="parse_detail",follow=False)
    )

    def parse_detail(self, response):
        title = response.xpath("//h1[@class='ph']/text()").get()
        author = response.xpath("//p[@class='authors']/a/text()").get()
        pub_time = response.xpath("//p[@class='authors']/span/text()").get()
        content = response.xpath("//td[@id='article_content']//text()").getall()
        item = WxspiderItem(title=title,author=author,pub_time=pub_time,content=content)
        yield item
        
