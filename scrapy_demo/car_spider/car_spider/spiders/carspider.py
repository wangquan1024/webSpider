# -*- coding: utf-8 -*-
import scrapy
from car_spider.items import CarSpiderItem
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class CarspiderSpider(CrawlSpider):
    name = 'carspider'
    allowed_domains = ['autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html#pvareaid=3454438']

    rules = (
        Rule(LinkExtractor(allow=r'https://car.autohome.com.cn/pic/series/65.+'),callback='parse_detail',follow=True),
    )

    def parse_detail(self, response):
        # 返回时的selectList类型，
        contentDivs = response.xpath("//div[@class='uibox']")
        for content in contentDivs:
            title = content.xpath("./div[@class='uibox-title']/a/text()").get()
            img_urls = content.xpath(".//li//img/@src").getall()
            image_urls = list(map(lambda url:response.urljoin(url).replace("240x180_0_q95_c42_",""),img_urls))
            item = CarSpiderItem(title=title,image_urls=image_urls)
            yield item
