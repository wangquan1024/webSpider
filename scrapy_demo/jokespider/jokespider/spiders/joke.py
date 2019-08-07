# -*- coding: utf-8 -*-
import scrapy
from jokespider.items import JokespiderItem


class JokeSpider(scrapy.Spider):
    name = 'joke'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_domain = "https://www.qiushibaike.com"

    def parse(self, response):
        # 返回时selectList类型
        # /选取儿子节点，不是子孙节点
        jokeDivs = response.xpath("//div[@id='content-left']/div")
        # 返回时selector类型，可以继续使用xpath方法
        # get方法返回选中内容的unicode字符串

        for jokeDiv in jokeDivs:
            author = jokeDiv.xpath('.//div[@class="author clearfix"]//h2/text()').get().strip()
            content = jokeDiv.xpath(".//div[@class='content']/span/text()").getall()
            content = "".join(content).strip()
            item = JokespiderItem(author=author,content=content)
            yield item
        next_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get()
        if not next_url:
            return
        else:
            # 再次请求
            yield scrapy.Request(self.base_domain+next_url,callback=self.parse)
