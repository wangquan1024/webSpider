# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from bossSpider.items import BossspiderItem


class BossSpiderSpider(CrawlSpider):
    name = 'boss_spider'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python&city=101200100&industry=&position=']

    rules = (
        # 匹配职位列表的规则
        Rule(LinkExtractor(allow=r'.+\?query=python&page=\d+'), follow=True),
        # 匹配职位详情页的规则
        Rule(LinkExtractor(allow=r'.+/job_detail/.+\.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        title = response.xpath("//div[@class='info-primary']//h1/text()").get()
        salary = response.xpath("//span[@class='salary']/text()").get()
        job_info = response.xpath("//div[@class='job-banner']//div[@class='info-primary']//p/text()").getall()
        city = job_info[0]
        work_years = job_info[1]
        education = job_info[2]
        company = response.xpath("//div[@class='smallbanner']//div[@class='info']/text()").get().strip()
        item = BossspiderItem(title=title,salary=salary,city=city,work_years=work_years,education=education,company=company)
        yield item