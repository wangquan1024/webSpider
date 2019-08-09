# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jianshu_spider.items import JianshuSpiderItem

class JianshuSpider(CrawlSpider):
    name = 'jianshu'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com']

    # 匹配规则不能写错
    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        title = response.xpath("//h1[@class='title']/text()").get()
        avatar = response.xpath("//a[@class='avatar']/img/@src").get()
        author = response.xpath("//span[@class='name']/a/text()").get()
        pub_time = response.xpath("//span[@class='publish-time']/text()").get()
        url = response.url
        url1 = url.split('?')[0]
        article_id = url1.split('/')[-1]

        content = response.xpath("//div[@class='show-content']").get()

        word_count =response.xpath("//span[@class='wordage']/text()").get()
        comment_count = response.xpath("//span[@class='comments-count']/text()").get()
        read_count = response.xpath("//span[@class='views-count']/text()").get()
        like_count = response.xpath("//span[@class='likes-count']/text()").get()

        subjects = ",".join(response.xpath("//div[@class='include-collection']/a/div/text()").getall())

        item = JianshuSpiderItem(title=title,avatar=avatar,author=author,
        pub_time=pub_time,origin_url=url,article_id=article_id,content=content,
        word_count=word_count,comment_count=comment_count,read_count=read_count,like_count=like_count,subjects=subjects)
        yield item